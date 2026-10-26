# path

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The current path to use when drawing the overlay.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayPathRenderer`](../mkoverlaypathrenderer.md) object instead.

## Declaration

```objc
@property CGPathRef path;
```

#### Discussion

Getting the value of this property causes the path to be created (using the [`createPath`](./createpath.md) method) if it does not already exist. You can also assign a path object to this property explicitly.

When assigning a new path object to this property, the receiver retains the path you specify.

## See Also

### Creating and managing the path
- [- createPath](./createpath.md)
  Creates the path for the overlay.
- [- invalidatePath](./invalidatepath.md)
  Releases the path associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/path)*