# SearchSuggestionsPlacement

**Framework**: SwiftUI  
**Kind**: struct

The ways that SwiftUI displays search suggestions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct SearchSuggestionsPlacement
```

#### Overview

You can influence which modes SwiftUI displays search suggestions for by using the [`searchSuggestions(_:for:)`](view/searchsuggestions(_:for:).md) modifier:

```swift
enum FruitSuggestion: String, Identifiable {
    case apple, banana, orange
    var id: Self { self }
}

@State private var text = ""
@State private var suggestions: [FruitSuggestion] = []

var body: some View {
    MainContent()
        .searchable(text: $text) {
            ForEach(suggestions) { suggestion in
                Text(suggestion.rawValue)
                    .searchCompletion(suggestion.rawValue)
            }
            .searchSuggestions(.hidden, for: .content)
        }
}
```

In the above example, SwiftUI only displays search suggestions in a suggestions menu. You might want to do this when you want to render search suggestions in a container, like inline with your own set of search results.

You can get the current search suggestion placement by querying the [`searchSuggestionsPlacement`](environmentvalues/searchsuggestionsplacement.md) environment value in your search suggestions.

## Topics

### Getting placements
- [static var automatic: SearchSuggestionsPlacement](searchsuggestionsplacement/automatic.md)
  Search suggestions render automatically based on the surrounding context.
- [static var content: SearchSuggestionsPlacement](searchsuggestionsplacement/content.md)
  Search suggestions render in the main content of the app.
- [static var menu: SearchSuggestionsPlacement](searchsuggestionsplacement/menu.md)
  Search suggestions render inside of a menu attached to the search field.
### Supporting types
- [SearchSuggestionsPlacement.Set](searchsuggestionsplacement/set.md)
  An efficient set of search suggestion display modes.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Suggesting search terms](suggesting-search-terms.md)
  Provide suggestions to people searching for content in your app.
- [func searchSuggestions<S>(() -> S) -> some View](view/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) -> some View](view/searchsuggestions(_:for:).md)
  Configures how to display search suggestions within this view.
- [func searchCompletion(_:)](view/searchcompletion(_:).md)
  Associates a fully formed string with the value of this view when used as a search suggestion.
- [func searchable(text:tokens:suggestedTokens:placement:prompt:token:)](view/searchable(text:tokens:suggestedtokens:placement:prompt:token:).md)
  Marks this view as searchable with text, tokens, and suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchsuggestionsplacement)*