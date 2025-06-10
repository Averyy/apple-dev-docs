# textField(_:provideUpdatedSuggestions:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Called when the text field’s text (or tokens) have changed and when the text field is going to display a new list of suggestion items.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
func textField(_ textField: NSTextField, provideUpdatedSuggestions responseHandler: @escaping (Self.ItemResponse) -> Void)
```

#### Discussion

Read the contents of `textField` to determine what suggestions to provide. For example:

```None
func textField(
    _ textField: NSTextField,
    provideUpdatedSuggestions responseHandler: @escaping ((ItemResponse) -> Void)
) {
    // 1. Get the results (filter).
    let searchString = textField.stringValue
    let matchedLocations = self.favoriteLocations.filter({
        $0.matches(searchString: searchString)
    }).prefix(5)

    // 2. Create item representations for the results.
    let items = matchedLocations.map({
        Item(representedValue: $0, title: $0.title)
    })

    // 3. Provide them back to the text field in a titled section.
    let response = ItemResponse(itemSections: [
        ItemSection(
            title: NSLocalizedString("Favorites", comment: …),
            items: items
        ),
    ])
    responseHandler(response)
}
```

If some of the suggestions are time-consuming to compute, or need to be fetched from an asynchronous/remote source, call `responseHandler` an additional time when that data has been fetched and processed.

```None
func textField(
    _ textField: NSTextField,
    provideUpdatedSuggestions responseHandler: @escaping ((ItemResponse) -> Void)
) {
    // …

    var response = ItemResponse(…)
    response.phase = .intermediate
    responseHandler(response)

    Task {
        let suggestedLocations = await LocationSuggestionsProvider.shared.suggestedLocations(for: searchString)

        response.itemSections.append(ItemSection(
            title: NSLocalizedString("Suggested Locations", comment: …),
            items: suggestedLocations.map({
                Item(representedValue: $0, title: $0.title)
            })
        ))
        response.phase = .final
        responseHandler(response)
    }
}
```

> **Note**: `responseHandler` must be called on the main thread. This can be (and should be for best user experience) called once synchronously from this function call to provide immediate response to the user typing in text. But, it can optionally be called additional times later if more results can be provided asynchronously (such as making a network request). Note that this closure is unique each time this function is called. Invoking a previously-provided closure will be ignored, therefore not negatively impacting the results the user sees by displaying results incongruous to the text field’s contents. If possible, it’s a good idea to cancel any long-running or expensive operations called for previous search requests when this function is called again.

> **Note**: This function is automatically called when the text field’s text or tokens change and the system determines that new suggestions are needed. This function may or may not be called with a delay for debouncing purposes.

## Parameters

- `textField`: The text field requesting updated suggestions.
- `responseHandler`: A closure to call with an item response when results have been gathered and are ready to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextsuggestionsdelegate/textfield(_:provideupdatedsuggestions:))*