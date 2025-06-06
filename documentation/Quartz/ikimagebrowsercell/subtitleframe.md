# subtitleFrame()

**Framework**: Quartz  
**Kind**: method

Returns the receiver’s subtitle frame rectangle.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func subtitleFrame() -> NSRect
```

#### Return Value

The coordinates of the subtitle frame, in the `IKImageBrowserView` coordinate space.

#### Discussion

It is the developer’s responsibility to compute the `subtitleFrame` such that it lies entirely within the cell’s [`frame()`](ikimagebrowsercell/frame().md) rectangle.

Subclasses can override this method to customize the position of the subtitle.

## See Also

- [func frame() -> NSRect](ikimagebrowsercell/frame.md)
  Returns the receiver’s frame rectangle, which defines its position in its [`IKImageBrowserView`](ikimagebrowserview.md).
- [func imageFrame() -> NSRect](ikimagebrowsercell/imageframe.md)
  Returns the receiver’s image frame rectangle, which defines the position of the thumbnail in its [`IKImageBrowserView`](ikimagebrowserview.md).
- [func titleFrame() -> NSRect](ikimagebrowsercell/titleframe.md)
  Returns the receiver’s title frame rectangle.
- [func imageContainerFrame() -> NSRect](ikimagebrowsercell/imagecontainerframe.md)
  Returns the receiver’s image container frame rectangle, which defines the position of the container of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/subtitleframe())*