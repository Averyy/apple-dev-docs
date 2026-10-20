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

If the view doesn’t have a well-defined transform, such as if it’s affected by a projection transform, this function may return `nil`.

## See Also

### Accessing geometry characteristics
- [func frame(in: some CoordinateSpaceProtocol) -> Rect3D](./frame%28in%29.md)
  The container view’s bounds rectangle converted to a defined coordinate space.
- [var size: Size3D](./size.md)
  The size of the container view.
- [var safeAreaInsets: EdgeInsets3D](./safeareainsets.md)
  The safe area inset of the container view.
- [subscript<T>(Anchor<T>) -> T](./subscript%28_%29.md)
  Resolves the value of an anchor to the container view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy3d/transform(in:))*