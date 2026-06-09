# searchToolbarBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the behavior for search in the toolbar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func searchToolbarBehavior(_ behavior: SearchToolbarBehavior) -> some View
```

#### Discussion

This modifier can be used to change the default behavior of a search field that appears in the toolbar. Place this modifier after the [`searchable(text:isPresented:placement:prompt:)`](view/searchable(text:ispresented:placement:prompt:).md) modifier that renders search in the toolbar.

On iPhone, the search field in the bottom toolbar can be configured to appear as a button-like control when inactive:

```swift
@State private var searchText = ""

NavigationStack {
    RecipeList()
        .searchable($searchText)
        .searchToolbarBehavior(.minimized)
}
```

## See Also

- [func searchable(text:placement:prompt:)](view/searchable(text:placement:prompt:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:isPresented:placement:prompt:)](view/searchable(text:ispresented:placement:prompt:).md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) -> some View](view/searchpresentationtoolbarbehavior(_:).md)
  Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [func searchSelection(Binding<TextSelection?>) -> some View](view/searchselection(_:).md)
  Binds the selection of the search field associated with the nearest searchable modifier to the given [`TextSelection`](textselection.md) value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchtoolbarbehavior(_:))*