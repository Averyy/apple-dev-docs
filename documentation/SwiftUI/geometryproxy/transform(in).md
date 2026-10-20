# transform(in:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

The container view’s 3D transform converted to a defined coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func transform(in coordinateSpace: some CoordinateSpaceProtocol) -> AffineTransform3D?
```

#### Discussion

If the view doesn’t have a well defined transform, such as if it is affected by a projection transform, this function may return `nil`.

## See Also

### Accessing geometry characteristics
- [func bounds(of: NamedCoordinateSpace) -> CGRect?](./bounds%28of%29.md)
  Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [var concentricCornerRadii: RectangleCornerRadii?](./concentriccornerradii.md)
  The concentric corner radii for this view’s bounds relative to the container shape.
- [func concentricCornerRadii(in: CGRect) -> RectangleCornerRadii?](./concentriccornerradii%28in%29.md)
  Returns the concentric corner radii for the specified frame relative to the container shape.
- [var containerCornerInsets: RectangleCornerInsets](./containercornerinsets.md)
  Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [var size: CGSize](./size.md)
  The size of the container view.
- [var safeAreaInsets: EdgeInsets](./safeareainsets.md)
  The safe area inset of the container view.
- [subscript<T>(Anchor<T>) -> T](./subscript%28_%29.md)
  Resolves the value of an anchor to the container view.
- [func frame(in:)](./frame%28in%29.md)
  Returns the container view’s bounds rectangle, converted to a defined coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy/transform(in:))*