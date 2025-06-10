# scrollEdgeEffectDisabled(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Disables any scroll edge effects for scroll views within this hierarchy.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func scrollEdgeEffectDisabled(_ disabled: Bool = true, for edges: Edge.Set = .all) -> some View
```

#### Discussion

By default, a scroll view will render an automatic edge effect style. You use this modifier to disable the rendering of any edge effects for scroll views within this hierarchy.

```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectDisabled()
```

## See Also

- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](view/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [struct ScrollEdgeEffectStyle](scrolledgeeffectstyle.md)
  A structure that defines the style of pocket a scroll view will have.
- [func safeAreaBar(edge:alignment:spacing:content:)](view/safeareabar(edge:alignment:spacing:content:).md)
  Renders the provided content appropriately to be displayed as a custom bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolledgeeffectdisabled(_:for:))*