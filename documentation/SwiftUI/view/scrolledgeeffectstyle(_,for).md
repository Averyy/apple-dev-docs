# scrollEdgeEffectStyle(_:for:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the scroll edge effect style for scroll views within this hierarchy.

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
func scrollEdgeEffectStyle(_ style: ScrollEdgeEffectStyle?, for edges: Edge.Set) -> some View
```

#### Discussion

By default, a scroll view renders an automatic edge effect. Use this modifier to change the scroll edge effect style.

```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectStyle(.hard, for: .all)
```

## See Also

### Configuring scroll edge effects
- [func scrollEdgeEffectHidden(Bool, for: Edge.Set) -> some View](./scrolledgeeffecthidden%28_,for%29.md)
  Hides any scroll edge effects for scroll views within this hierarchy.
- [struct ScrollEdgeEffectStyle](../scrolledgeeffectstyle.md)
  A structure that specifies blur transitions between scrolling content and an area with controls, such as toolbars.
- [func safeAreaBar(edge:alignment:spacing:content:)](./safeareabar%28edge,alignment,spacing,content%29.md)
  Shows the specified content as a custom bar beside the modified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolledgeeffectstyle(_:for:))*