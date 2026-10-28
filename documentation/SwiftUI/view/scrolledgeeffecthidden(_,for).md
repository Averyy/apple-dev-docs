# scrollEdgeEffectHidden(_:for:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Hides any scroll edge effects for scroll views within this hierarchy.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func scrollEdgeEffectHidden(_ hidden: Bool = true, for edges: Edge.Set = .all) -> some View
```

## Discussion

By default, a scroll view renders an automatic edge effect style. Use this modifier to hide any edge effects for scroll views within this hierarchy.

```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectHidden()
```

## See Also

### Configuring scroll edge effects
- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](./scrolledgeeffectstyle%28_,for%29.md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [struct ScrollEdgeEffectStyle](../scrolledgeeffectstyle.md)
  A structure that specifies blur transitions between scrolling content and an area with controls, such as toolbars.
- [func safeAreaBar(edge:alignment:spacing:content:)](./safeareabar%28edge,alignment,spacing,content%29.md)
  Shows the specified content as a custom bar beside the modified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolledgeeffecthidden(_:for:))*