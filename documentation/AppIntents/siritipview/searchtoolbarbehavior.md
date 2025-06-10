# searchToolbarBehavior(_:)

**Framework**: App Intents  
**Kind**: method

Configures the behavior for search in the toolbar.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func searchToolbarBehavior(_ behavior: SearchToolbarBehavior) -> some View
```

#### Discussion

This modifier can be used to change the default behavior of a search field that appears in the toolbar. Place this modifier after the `View/searchable(text:isPresented:placement:prompt:)` modifier that renders search in the toolbar.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/searchtoolbarbehavior(_:))*