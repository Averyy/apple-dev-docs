# scrollEdgeEffectStyle(_:for:)

**Framework**: SwiftUI  
**Kind**: method

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

- [func scrollEdgeEffectHidden(Bool, for: Edge.Set) -> some View](view/scrolledgeeffecthidden(_:for:).md)
  Hides any scroll edge effects for scroll views within this hierarchy.
- [struct ScrollEdgeEffectStyle](scrolledgeeffectstyle.md)
  A structure that defines the style of pocket a scroll view will have.
- [func safeAreaBar(edge:alignment:spacing:content:)](view/safeareabar(edge:alignment:spacing:content:).md)
  Shows the specified content as a custom bar beside the modified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolledgeeffectstyle(_:for:))*