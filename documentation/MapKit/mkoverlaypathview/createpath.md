# createPath

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Creates the path for the overlay.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayPathRenderer`](../mkoverlaypathrenderer.md) object instead.

## Declaration

```objc
- (void) createPath;
```

#### Discussion

The default implementation of this method does nothing. Subclasses should override it and use it to create the [`CGPath`](../../CoreGraphics/cgpath.md) data type to be used for drawing. After creating the path, your implementation should then assign it to the [`path`](./path.md) property.

## See Also

### Creating and managing the path
- [path](./path.md)
  The current path to use when drawing the overlay.
- [- invalidatePath](./invalidatepath.md)
  Releases the path associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/createpath)*