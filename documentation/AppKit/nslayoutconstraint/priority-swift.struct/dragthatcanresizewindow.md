# dragThatCanResizeWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Appropriate priority level for a drag that may end up resizing the window.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var dragThatCanResizeWindow: NSLayoutConstraint.Priority { get }
```

```c
static const NSLayoutPriority NSLayoutPriorityDragThatCanResizeWindow;
```

## Discussion

This drag does not need to explicitly resize the window. The user might be dragging around window contents, and it might be desirable for the window get bigger to accommodate those contents.

## See Also

### Constants
- [static var required: NSLayoutConstraint.Priority](./required.md)
  A required constraint.
- [static var defaultHigh: NSLayoutConstraint.Priority](./defaulthigh.md)
  Priority level with which a button resists compressing its content.
- [static var windowSizeStayPut: NSLayoutConstraint.Priority](./windowsizestayput.md)
  Priority level for the window’s current size.
- [static var dragThatCannotResizeWindow: NSLayoutConstraint.Priority](./dragthatcannotresizewindow.md)
  Priority level at which a split view divider, say, is dragged.
- [static var defaultLow: NSLayoutConstraint.Priority](./defaultlow.md)
  Priority level at which a button hugs its contents horizontally.
- [static var fittingSizeCompression: NSLayoutConstraint.Priority](./fittingsizecompression.md)
  When you send a [`fittingSize`](../../nsview/fittingsize.md) message to a view, the smallest size that is large enough for the view’s contents is computed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority-swift.struct/dragthatcanresizewindow)*