# bounds(of:)

**Framework**: SwiftUI  
**Kind**: method

Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.

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
func bounds(of coordinateSpace: NamedCoordinateSpace) -> CGRect?
```

## See Also

- [var concentricCornerRadii: RectangleCornerRadii?](geometryproxy/concentriccornerradii.md)
  The concentric corner radii for this view’s bounds relative to the container shape.
- [func concentricCornerRadii(in: CGRect) -> RectangleCornerRadii?](geometryproxy/concentriccornerradii(in:).md)
  Returns the concentric corner radii for the specified frame relative to the container shape.
- [var containerCornerInsets: RectangleCornerInsets](geometryproxy/containercornerinsets.md)
  Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [func frame(in:)](geometryproxy/frame(in:).md)
  Returns the container view’s bounds rectangle, converted to a defined coordinate space.
- [var size: CGSize](geometryproxy/size.md)
  The size of the container view.
- [var safeAreaInsets: EdgeInsets](geometryproxy/safeareainsets.md)
  The safe area inset of the container view.
- [subscript<T>(Anchor<T>) -> T](geometryproxy/subscript(_:).md)
  Resolves the value of an anchor to the container view.
- [func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?](geometryproxy/transform(in:).md)
  The container view’s 3D transform converted to a defined coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy/bounds(of:))*