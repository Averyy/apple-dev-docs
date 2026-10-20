# draggingFrame

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The frame of the dragging item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var draggingFrame: NSRect { get set }
```

```objc
@property NSRect draggingFrame;
```

#### Discussion

The dragging frame provides the spatial relationship between [`NSDraggingItem`](../nsdraggingitem.md) instances when you set the dragging formation to [`NSDraggingFormation.none`](../nsdraggingformation/none.md).

The exact coordinate space of this rectangle depends on where you use it. Examples are the view that initiates the drag using [`beginDraggingSession(with:event:source:)`](../nsview/begindraggingsession%28with,event,source%29.md) or the view you pass to the [`NSDraggingSession`](../nsdraggingsession.md) implementation of [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](../nsdraggingsession/enumeratedraggingitems%28options,for,classes,searchoptions,using%29.md).

## See Also

### Dragging frame
- [func setDraggingFrame(NSRect, contents: Any?)](./setdraggingframe%28_,contents%29.md)
  Sets the item’s dragging frame and contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/draggingframe)*