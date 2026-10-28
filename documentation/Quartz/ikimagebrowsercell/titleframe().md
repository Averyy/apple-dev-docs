# titleFrame()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s title frame rectangle.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func titleFrame() -> NSRect
```

```objc
- (NSRect) titleFrame;
```

## Return Value

The coordinates of the title frame, in the `IKImageBrowserView` coordinate space.

## Discussion

It is the developer’s responsibility to compute the `titleFrame` such that it lies entirely within the cell’s [`frame()`](./frame%28%29.md) rectangle.

Subclasses can override this method to customize the position of the title.

## See Also

### Cell Component Frames
- [func frame() -> NSRect](./frame%28%29.md)
  Returns the receiver’s frame rectangle, which defines its position in its [`IKImageBrowserView`](../ikimagebrowserview.md).
- [func imageFrame() -> NSRect](./imageframe%28%29.md)
  Returns the receiver’s image frame rectangle, which defines the position of the thumbnail in its [`IKImageBrowserView`](../ikimagebrowserview.md).
- [func subtitleFrame() -> NSRect](./subtitleframe%28%29.md)
  Returns the receiver’s subtitle frame rectangle.
- [func imageContainerFrame() -> NSRect](./imagecontainerframe%28%29.md)
  Returns the receiver’s image container frame rectangle, which defines the position of the container of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/titleframe())*