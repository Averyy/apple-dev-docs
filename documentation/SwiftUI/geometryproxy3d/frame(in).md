# frame(in:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

The container view’s bounds rectangle converted to a defined coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func frame(in coordinateSpace: some CoordinateSpaceProtocol) -> Rect3D
```

## See Also

### Accessing geometry characteristics
- [var size: Size3D](./size.md)
  The size of the container view.
- [var safeAreaInsets: EdgeInsets3D](./safeareainsets.md)
  The safe area inset of the container view.
- [subscript<T>(Anchor<T>) -> T](./subscript%28_%29.md)
  Resolves the value of an anchor to the container view.
- [func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?](./transform%28in%29.md)
  The container view’s 3D transform converted to a defined coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy3d/frame(in:))*