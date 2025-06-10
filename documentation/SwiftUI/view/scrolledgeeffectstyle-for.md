# scrollEdgeEffectStyle(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Configures the scroll edge effect style for scroll views within this hierarchy.

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
func scrollEdgeEffectStyle(_ style: ScrollEdgeEffectStyle?, for edges: Edge.Set) -> some View
```

#### Discussion

By default, a scroll view will render an automatic edge effect. You use this modifier to change rendered edge effect style.

```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectStyle(.hard)
```

## See Also

- [func scrollEdgeEffectDisabled(Bool, for: Edge.Set) -> some View](view/scrolledgeeffectdisabled(_:for:).md)
  Disables any scroll edge effects for scroll views within this hierarchy.
- [struct ScrollEdgeEffectStyle](scrolledgeeffectstyle.md)
  A structure that defines the style of pocket a scroll view will have.
- [func safeAreaBar(edge:alignment:spacing:content:)](view/safeareabar(edge:alignment:spacing:content:).md)
  Renders the provided content appropriately to be displayed as a custom bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolledgeeffectstyle(_:for:))*