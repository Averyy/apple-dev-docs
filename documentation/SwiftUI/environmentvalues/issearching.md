# isSearching

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates when the user is searching.

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
var isSearching: Bool { get }
```

## Mentions

- [Managing search interface activation](managing-search-interface-activation.md)

#### Discussion

You can read this value like any of the other [`EnvironmentValues`](environmentvalues.md), by creating a property with the [`Environment`](environment.md) property wrapper:

```swift
@Environment(\.isSearching) private var isSearching
```

Get the value to find out when the user interacts with a search field that’s produced by one of the searchable modifiers, like [`searchable(text:placement:prompt:)`](view/searchable(text:placement:prompt:).md):

```swift
struct SearchingExample: View {
    @State private var searchText = ""

    var body: some View {
        NavigationStack {
            SearchedView()
                .searchable(text: $searchText)
        }
    }
}

struct SearchedView: View {
    @Environment(\.isSearching) private var isSearching

    var body: some View {
        Text(isSearching ? "Searching!" : "Not searching.")
    }
}
```

When the user first taps or clicks in a search field, the `isSearching` property becomes `true`. When the user cancels the search operation, the property becomes `false`. To programmatically set the value to `false` and dismiss the search operation, use [`dismissSearch`](environmentvalues/dismisssearch.md).

> ❗ **Important**: Access the value from inside the searched view, as the example above demonstrates, rather than from the searched view’s parent. SwiftUI sets the value in the environment of the view that you apply the searchable modifier to, and doesn’t propagate the value up the view hierarchy.

## See Also

- [Managing search interface activation](managing-search-interface-activation.md)
  Programmatically detect and dismiss a search field.
- [var dismissSearch: DismissSearchAction](environmentvalues/dismisssearch.md)
  An action that ends the current search interaction.
- [struct DismissSearchAction](dismisssearchaction.md)
  An action that can end a search interaction.
- [func searchable(text:isPresented:placement:prompt:)](view/searchable(text:ispresented:placement:prompt:).md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text:tokens:isPresented:placement:prompt:token:)](view/searchable(text:tokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable(text:editableTokens:isPresented:placement:prompt:token:)](view/searchable(text:editabletokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](view/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/issearching)*