# searchCompletion(_:)

**Framework**: SwiftUI  
**Kind**: method

Associates a fully formed string with the value of this view when used as a search suggestion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func searchCompletion(_ completion: String) -> some View
```

## Mentions

- [Suggesting search terms](suggesting-search-terms.md)

#### Discussion

Use this method to associate a fully formed string with a view that is within a search suggestion list context. The system uses this value when the view is selected to replace the partial text being currently edited of the associated search field.

On tvOS, the string that you provide to the this modifier is used when displaying the associated suggestion and when replacing the partial text of the search field.

```swift
SearchPlaceholderView()
    .searchable(text: $text) {
        Text("🍎").searchCompletion("apple")
        Text("🍐").searchCompletion("pear")
        Text("🍌").searchCompletion("banana")
    }
```

## See Also

- [Suggesting search terms](suggesting-search-terms.md)
  Provide suggestions to people searching for content in your app.
- [func searchSuggestions<S>(() -> S) -> some View](view/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) -> some View](view/searchsuggestions(_:for:).md)
  Configures how to display search suggestions within this view.
- [func searchable(text:tokens:suggestedTokens:placement:prompt:token:)](view/searchable(text:tokens:suggestedtokens:placement:prompt:token:).md)
  Marks this view as searchable with text, tokens, and suggestions.
- [struct SearchSuggestionsPlacement](searchsuggestionsplacement.md)
  The ways that SwiftUI displays search suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchcompletion(_:))*