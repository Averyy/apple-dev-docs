# frame()

**Framework**: Quartz  
**Kind**: method

Returns the receiver’s frame rectangle, which defines its position in its [`IKImageBrowserView`](ikimagebrowserview.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
func frame() -> NSRect
```

#### Return Value

The coordinates of the frame, in the `IKImageBrowserView` coordinate space.

#### Discussion

Subclasses should not override this method.

## See Also

- [func imageFrame() -> NSRect](ikimagebrowsercell/imageframe.md)
  Returns the receiver’s image frame rectangle, which defines the position of the thumbnail in its [`IKImageBrowserView`](ikimagebrowserview.md).
- [func subtitleFrame() -> NSRect](ikimagebrowsercell/subtitleframe.md)
  Returns the receiver’s subtitle frame rectangle.
- [func titleFrame() -> NSRect](ikimagebrowsercell/titleframe.md)
  Returns the receiver’s title frame rectangle.
- [func imageContainerFrame() -> NSRect](ikimagebrowsercell/imagecontainerframe.md)
  Returns the receiver’s image container frame rectangle, which defines the position of the container of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/frame())*