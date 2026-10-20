# frame()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s frame rectangle, which defines its position in its [`IKImageBrowserView`](../ikimagebrowserview.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
func frame() -> NSRect
```

```objc
- (NSRect) frame;
```

#### Return Value

The coordinates of the frame, in the `IKImageBrowserView` coordinate space.

#### Discussion

Subclasses should not override this method.

## See Also

### Cell Component Frames
- [func imageFrame() -> NSRect](./imageframe%28%29.md)
  Returns the receiver’s image frame rectangle, which defines the position of the thumbnail in its [`IKImageBrowserView`](../ikimagebrowserview.md).
- [func subtitleFrame() -> NSRect](./subtitleframe%28%29.md)
  Returns the receiver’s subtitle frame rectangle.
- [func titleFrame() -> NSRect](./titleframe%28%29.md)
  Returns the receiver’s title frame rectangle.
- [func imageContainerFrame() -> NSRect](./imagecontainerframe%28%29.md)
  Returns the receiver’s image container frame rectangle, which defines the position of the container of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/frame())*