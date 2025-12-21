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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchtoolbarbehavior(_:))*