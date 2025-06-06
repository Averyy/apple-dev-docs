# position(_:)

**Framework**: SwiftUI  
**Kind**: method

Positions the center of this view at the specified point in its parent’s coordinate space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func position(_ position: CGPoint) -> some View
```

#### Return Value

A view that fixes the center of this view at `position`.

#### Discussion

Use the `position(_:)` modifier to place the center of a view at a specific coordinate in the parent view using a [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) to specify the `x` and `y` offset.

```swift
Text("Position by passing a CGPoint()")
    .position(CGPoint(x: 175, y: 100))
    .border(Color.gray)
```

## Parameters

- `position`: The point at which to place the center of this   view.

## See Also

- [Making fine adjustments to a view’s position](making-fine-adjustments-to-a-view-s-position.md)
  Shift the position of a view by applying the offset or position modifier.
- [func position(x: CGFloat, y: CGFloat) -> some View](view/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func offset(CGSize) -> some View](view/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](view/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.
- [func offset(z: CGFloat) -> some View](view/offset(z:).md)
  Brings a view forward in Z by the provided distance in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/position(_:))*