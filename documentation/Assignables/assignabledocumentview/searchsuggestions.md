# searchSuggestions(_:)

**Framework**: Assignables  
**Kind**: method

Configures the search suggestions for this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func searchSuggestions<S>(@ViewBuilder _ suggestions: () -> S) -> some View where S : View
```

#### Discussion

You can suggest search terms during a search operation by providing a collection of view to this modifier. The interface presents the suggestion views as a list of choices when someone activates the search interface. Associate a string with each suggestion view by adding the `View/searchCompletion(_:)` modifier to the view. For example, you can suggest fruit types by displaying their emoji, and provide the corresponding search string as a search completion in each case:

```None
ProductList()
    .searchable(text: $text)
    .searchSuggestions {
        Text("🍎").searchCompletion("apple")
        Text("🍐").searchCompletion("pear")
        Text("🍌").searchCompletion("banana")
    }
```

When someone chooses a suggestion, SwiftUI replaces the text in the search field with the search completion string. If you omit the search completion modifier for a particular suggestion view, SwiftUI displays the suggestion, but the suggestion view doesn’t react to taps or clicks.

> ❗ **Important**: In tvOS, searchable modifiers only support suggestion views of type `Text`, like in the above example. Other platforms can use any view for the suggestions, including custom views.

You can update the suggestions that you provide as conditions change.

For example, you can specify an array of suggestions that you store in a model:

```None
ProductList()
    .searchable(text: $text)
    .searchSuggestions {
        ForEach(model.suggestedSearches) { suggestion in
            Label(suggestion.title, image: suggestion.image)
                .searchCompletion(suggestion.text)
        }
    }
```

If the model’s `suggestedSearches` begins as an empty array, the interface doesn’t display any suggestions to start. You can then provide logic that updates the array based on some condition. For example, you might update the completions based on the current search text. Note that certain events or actions, like when someone moves a macOS window, might dismiss the suggestion view.

For more information about using search modifiers, see doc:Adding-a-search-interface-to-your-app.

## Parameters

- `suggestions`: A view builder that produces content that   populates a list of suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/searchsuggestions(_:))*