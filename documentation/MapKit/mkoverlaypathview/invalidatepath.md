# invalidatePath

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Releases the path associated with the receiver.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayPathRenderer`](../mkoverlaypathrenderer.md) object instead.

## Declaration

```objc
- (void) invalidatePath;
```

#### Discussion

You can call this method at any time where a change in the path information would require you to recreate the path. This method sets the [`path`](./path.md) property to `nil`, which causes the cached path to be released.

## See Also

### Creating and managing the path
- [path](./path.md)
  The current path to use when drawing the overlay.
- [- createPath](./createpath.md)
  Creates the path for the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/invalidatepath)*