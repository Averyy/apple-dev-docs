# imageFrame()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s image frame rectangle, which defines the position of the thumbnail in its [`IKImageBrowserView`](../ikimagebrowserview.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
func imageFrame() -> NSRect
```

```objc
- (NSRect) imageFrame;
```

## Return Value

The coordinates of the frame, in the `IKImageBrowserView` coordinate space.

## Discussion

It is the developer’s responsibility to compute the `imageFrame` such that it lies entirely within the cell’s [`frame()`](./frame%28%29.md) rectangle.

Subclasses can override this method to customize the position of the thumbnail.

## See Also

### Cell Component Frames
- [func frame() -> NSRect](./frame%28%29.md)
  Returns the receiver’s frame rectangle, which defines its position in its [`IKImageBrowserView`](../ikimagebrowserview.md).
- [func subtitleFrame() -> NSRect](./subtitleframe%28%29.md)
  Returns the receiver’s subtitle frame rectangle.
- [func titleFrame() -> NSRect](./titleframe%28%29.md)
  Returns the receiver’s title frame rectangle.
- [func imageContainerFrame() -> NSRect](./imagecontainerframe%28%29.md)
  Returns the receiver’s image container frame rectangle, which defines the position of the container of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/imageframe())*