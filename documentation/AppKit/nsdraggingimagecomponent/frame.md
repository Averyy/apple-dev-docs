# frame

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The coordinate space is the bounds of the parent dragging item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var frame: NSRect { get set }
```

```objc
@property NSRect frame;
```

#### Discussion

The frame is {{0,0}, {`draggingFrame.size.width`, `draggingFrame.size.height`}}.

The coordinate space is the bounds of the parent [`NSDraggingItem`](../nsdraggingitem.md) instance’s [`draggingFrame`](../nsdraggingitem/draggingframe.md).

## See Also

### Related Documentation
- [var draggingFrame: NSRect](../nsdraggingitem/draggingframe.md)
  The frame of the dragging item.
### Dragging Image Contents
- [var contents: Any?](./contents.md)
  An object providing the image contents of the component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/frame)*