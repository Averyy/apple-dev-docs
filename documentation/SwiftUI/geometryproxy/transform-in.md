# transform(in:)

**Framework**: SwiftUI  
**Kind**: method

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

- [func bounds(of: NamedCoordinateSpace) -> CGRect?](geometryproxy/bounds(of:).md)
  Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [func frame(in:)](geometryproxy/frame(in:).md)
  Returns the container view’s bounds rectangle, converted to a defined coordinate space.
- [var size: CGSize](geometryproxy/size.md)
  The size of the container view.
- [var safeAreaInsets: EdgeInsets](geometryproxy/safeareainsets.md)
  The safe area inset of the container view.
- [subscript<T>(Anchor<T>) -> T](geometryproxy/subscript(_:).md)
  Resolves the value of an anchor to the container view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy/transform(in:))*