# searchPresentationToolbarBehavior(_:)

**Framework**: RealityKit  
**Kind**: method

Configures the search toolbar presentation behavior for any searchable modifiers within this view.

**Availability**:
- iOS 17.1+
- iPadOS 17.1+
- Mac Catalyst ?+
- macOS 14.1+
- tvOS 17.1+
- visionOS ?+
- watchOS 10.1+

## Declaration

```swift
nonisolated
func searchPresentationToolbarBehavior(_ behavior: SearchPresentationToolbarBehavior) -> some View
```

#### Discussion

By default on iOS, a toolbar may hide parts of its content when presenting search to focus on searching. You can override this behavior by providing a value of `SearchPresentationToolbarBehavior/avoidHidingContent` to this modifer.

```None
@State private var searchText = ""

List {
    // ... content
}
.searchable(text: $searchText)
.searchPresentationToolbarBehavior(.avoidHidingContent)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/searchpresentationtoolbarbehavior(_:))*