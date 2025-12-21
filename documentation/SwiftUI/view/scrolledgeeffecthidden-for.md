# scrollEdgeEffectHidden(_:for:)

**Framework**: SwiftUI  
**Kind**: method

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

#### Discussion

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

- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](view/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [struct ScrollEdgeEffectStyle](scrolledgeeffectstyle.md)
  A structure that defines the style of pocket a scroll view will have.
- [func safeAreaBar(edge:alignment:spacing:content:)](view/safeareabar(edge:alignment:spacing:content:).md)
  Shows the specified content as a custom bar beside the modified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolledgeeffecthidden(_:for:))*