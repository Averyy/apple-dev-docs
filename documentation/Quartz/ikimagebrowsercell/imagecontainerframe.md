# imageContainerFrame()

**Framework**: Quartz  
**Kind**: method

Returns the receiver’s image container frame rectangle, which defines the position of the container of the thumbnail.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func imageContainerFrame() -> NSRect
```

#### Return Value

The coordinates of image container frame, in the `IKImageBrowserView` coordinate space.

#### Discussion

The image frame is computed automatically from the image container frame by taking in account the image alignment and the image aspect ratio.

Subclasses can override this method to customize the position of the thumbnail container.

## See Also

- [func frame() -> NSRect](ikimagebrowsercell/frame.md)
  Returns the receiver’s frame rectangle, which defines its position in its [`IKImageBrowserView`](ikimagebrowserview.md).
- [func imageFrame() -> NSRect](ikimagebrowsercell/imageframe.md)
  Returns the receiver’s image frame rectangle, which defines the position of the thumbnail in its [`IKImageBrowserView`](ikimagebrowserview.md).
- [func subtitleFrame() -> NSRect](ikimagebrowsercell/subtitleframe.md)
  Returns the receiver’s subtitle frame rectangle.
- [func titleFrame() -> NSRect](ikimagebrowsercell/titleframe.md)
  Returns the receiver’s title frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/imagecontainerframe())*