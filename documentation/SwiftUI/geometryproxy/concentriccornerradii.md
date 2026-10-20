# concentricCornerRadii

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The concentric corner radii for this view’s bounds relative to the container shape.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var concentricCornerRadii: RectangleCornerRadii? { get }
```

#### Return Value

The resolved corner radii, or `nil` if no container shape is set or the shape does not provide sufficient corner info.

#### Discussion

Concentric corners share the same center point as the container’s corners, creating visually harmonious nested rounded rectangles. The radius for each corner is calculated as the container’s corner radius minus the distance from this view’s corner to the container’s corner.

Unlike [`ConcentricRectangle`](../concentricrectangle.md), which calculates and draws the shape, this property only returns the calculated radii. This allows you to use the values for custom drawing, animations, or other purposes:

```swift
GeometryReader { geometry in
    Canvas { context, size in
        if let radii = geometry.concentricCornerRadii {
            let path = Path(
                roundedRect: CGRect(origin: .zero, size: size),
                cornerRadii: radii
            )
            context.fill(path, with: .color(.blue))
        }
    }
}
.containerShape(.rect(cornerRadius: 48))
```

Each corner’s radius depends on its position relative to the container:

- Corners aligned with the container’s corners get concentric radii
- Corners far from the container’s corners get zero radii
- The radius is clamped to the view’s maximum possible radius

> **See Also**: [`ConcentricRectangle`](../concentricrectangle.md)

## See Also

### Accessing geometry characteristics
- [func bounds(of: NamedCoordinateSpace) -> CGRect?](./bounds%28of%29.md)
  Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
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
- [func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?](./transform%28in%29.md)
  The container view’s 3D transform converted to a defined coordinate space.
- [func frame(in:)](./frame%28in%29.md)
  Returns the container view’s bounds rectangle, converted to a defined coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy/concentriccornerradii)*