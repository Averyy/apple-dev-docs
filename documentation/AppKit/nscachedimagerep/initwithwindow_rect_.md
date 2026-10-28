# initWithWindow:rect:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a cached image representation initialized for drawing in the specified window.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```objc
- (id) initWithWindow:(NSWindow *) win rect:(NSRect) rect;
```

## Discussion

You must draw the image yourself in the designated part of the window. There are no `NSCachedImageRep` methods for this purpose.

## Parameters

- `win`: The window (typically offscreen) in which the image is to be rendered. The window is retained by the receiver.
- `rect`: The position and size of the image in the specified window. This rectangle should be specified in the base coordinate system of the window.

## See Also

### Related Documentation
- [var size: NSSize](../nsimagerep/size.md)
  The size of the image representation, measured in points in the user coordinate space.
### Initializing Cached Representations of Images
- [- initWithSize:depth:separate:alpha:](./initwithsize_depth_separate_alpha_.md)
  Returns a cached image representation initialized with the specified image characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscachedimagerep/initwithwindow:rect:)*