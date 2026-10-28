# position(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

## Return Value

A view that fixes the center of this view at `position`.

## Discussion

Use the `position(_:)` modifier to place the center of a view at a specific coordinate in the parent view using a [`CGPoint`](../../CoreFoundation/cgpoint.md) to specify the `x` and `y` offset.

```swift
Text("Position by passing a CGPoint()")
    .position(CGPoint(x: 175, y: 100))
    .border(Color.gray)
```

## Parameters

- `position`: The point at which to place the center of this view.

## See Also

### Adjusting a view’s position
- [Making fine adjustments to a view’s position](../making-fine-adjustments-to-a-view-s-position.md)
  Shift the position of a view by applying the offset or position modifier.
- [func position(x: CGFloat, y: CGFloat) -> some View](./position%28x,y%29.md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func offset(CGSize) -> some View](./offset%28_%29.md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](./offset%28x,y%29.md)
  Offset this view by the specified horizontal and vertical distances.
- [func offset(z: CGFloat) -> some View](./offset%28z%29.md)
  Brings a view forward in Z by the provided distance in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/position(_:))*