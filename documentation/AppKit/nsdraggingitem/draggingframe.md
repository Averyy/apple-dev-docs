# draggingFrame

**Framework**: AppKit  
**Kind**: property

The frame of the dragging item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var draggingFrame: NSRect { get set }
```

#### Discussion

The dragging frame provides the spatial relationship between [`NSDraggingItem`](nsdraggingitem.md) instances when you set the dragging formation to [`NSDraggingFormation.none`](nsdraggingformation/none.md).

The exact coordinate space of this rectangle depends on where you use it. Examples are the view that initiates the drag using [`beginDraggingSession(with:event:source:)`](nsview/begindraggingsession(with:event:source:).md) or the view you pass to the [`NSDraggingSession`](nsdraggingsession.md) implementation of [`enumerateDraggingItems(options:for:classes:searchOptions:using:)`](nsdraggingsession/enumeratedraggingitems(options:for:classes:searchoptions:using:).md).

## See Also

- [func setDraggingFrame(NSRect, contents: Any?)](nsdraggingitem/setdraggingframe(_:contents:).md)
  Sets the item’s dragging frame and contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitem/draggingframe)*