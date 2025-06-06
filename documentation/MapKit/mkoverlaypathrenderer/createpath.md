# createPath()

**Framework**: MapKit  
**Kind**: method

Creates the path for the overlay.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func createPath()
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it and use it to create the [`CGPath`](https://developer.apple.com/documentation/CoreGraphics/CGPath) data type the subclass uses for drawing. After creating the path, your implementation needs to assign it to the [`path`](mkoverlaypathrenderer/path.md) property.

## See Also

- [var path: CGPath!](mkoverlaypathrenderer/path.md)
  The path representing the overlay’s shape.
- [func invalidatePath()](mkoverlaypathrenderer/invalidatepath.md)
  Updates the path associated with the overlay renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/createpath())*