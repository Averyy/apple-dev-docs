# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Resolves the value of an anchor to the container view.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
subscript<T>(anchor: Anchor<T>) -> T { get }
```

## See Also

### Accessing geometry characteristics
- [func frame(in: some CoordinateSpaceProtocol) -> Rect3D](./frame%28in%29.md)
  The container view’s bounds rectangle converted to a defined coordinate space.
- [var size: Size3D](./size.md)
  The size of the container view.
- [var safeAreaInsets: EdgeInsets3D](./safeareainsets.md)
  The safe area inset of the container view.
- [func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?](./transform%28in%29.md)
  The container view’s 3D transform converted to a defined coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy3d/subscript(_:))*