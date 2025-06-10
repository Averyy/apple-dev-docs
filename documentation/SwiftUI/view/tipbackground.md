# tipBackground(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the tip’s view background to a style. Currently this only applies to inline tips, not popover tips.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func tipBackground<S>(_ style: S) -> some View where S : ShapeStyle
```

#### Return Value

A view with the specified style drawn behind it.

## Parameters

- `style`: An instance of a type that conforms to   that   SwiftUI draws behind the modified view.

## See Also

- [func popoverTip((any Tip)?, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:arrowedge:action:).md)
  Presents a popover tip on the modified view.
- [func tipCornerRadius(CGFloat, antialiased: Bool) -> some View](view/tipcornerradius(_:antialiased:).md)
  Sets the corner radius for an inline tip view.
- [func tipImageSize(CGSize) -> some View](view/tipimagesize(_:).md)
  Sets the size for a tip’s image.
- [func tipViewStyle(some TipViewStyle) -> some View](view/tipviewstyle(_:).md)
  Sets the given style for TipView within the view hierarchy.
- [func tipImageStyle<S>(S) -> some View](view/tipimagestyle(_:).md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2>(S1, S2) -> some View](view/tipimagestyle(_:_:).md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/tipimagestyle(_:_:_:).md)
  Sets the style for a tip’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tipbackground(_:))*