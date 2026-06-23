# concentricCornerRadii(in:)

**Framework**: SwiftUI  
**Kind**: method

Returns the concentric corner radii for the specified frame relative to the container shape.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func concentricCornerRadii(in frame: CGRect) -> RectangleCornerRadii?
```

#### Return Value

The resolved corner radii, or `nil` if no container shape is set or the shape does not provide sufficient corner info.

#### Discussion

Concentric corners share the same center point as the container’s corners. The radius for each corner is calculated as the container’s corner radius minus the distance from the frame’s corner to the container’s corner.

Unlike [`ConcentricRectangle`](concentricrectangle.md), which calculates and draws the shape, this function only returns the calculated radii. Use this when you need corner radii for a subregion of the view, or when you want to use the values for custom drawing, animations, or other purposes:

```swift
GeometryReader { geometry in
    Canvas { context, size in
        let rect = CGRect(x: 10, y: 10, width: 80, height: 80)
        if let radii = geometry.concentricCornerRadii(in: rect) {
            let path = Path(roundedRect: rect, cornerRadii: radii)
            context.fill(path, with: .color(.blue))
        }
    }
}
.containerShape(.rect(cornerRadius: 48))
```

> **Note**: [`ConcentricRectangle`](concentricrectangle.md)

## Parameters

- `frame`: The frame in the view’s local coordinate space for which to calculate the concentric corner radii.

## See Also

- [func bounds(of: NamedCoordinateSpace) -> CGRect?](geometryproxy/bounds(of:).md)
  Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [var concentricCornerRadii: RectangleCornerRadii?](geometryproxy/concentriccornerradii.md)
  The concentric corner radii for this view’s bounds relative to the container shape.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy/concentriccornerradii(in:))*