# defaultLow

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Priority level at which a button hugs its contents horizontally.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var defaultLow: NSLayoutConstraint.Priority { get }
```

```c
static const NSLayoutPriority NSLayoutPriorityDefaultLow;
```

## See Also

### Constants
- [static var required: NSLayoutConstraint.Priority](./required.md)
  A required constraint.
- [static var defaultHigh: NSLayoutConstraint.Priority](./defaulthigh.md)
  Priority level with which a button resists compressing its content.
- [static var dragThatCanResizeWindow: NSLayoutConstraint.Priority](./dragthatcanresizewindow.md)
  Appropriate priority level for a drag that may end up resizing the window.
- [static var windowSizeStayPut: NSLayoutConstraint.Priority](./windowsizestayput.md)
  Priority level for the window’s current size.
- [static var dragThatCannotResizeWindow: NSLayoutConstraint.Priority](./dragthatcannotresizewindow.md)
  Priority level at which a split view divider, say, is dragged.
- [static var fittingSizeCompression: NSLayoutConstraint.Priority](./fittingsizecompression.md)
  When you send a [`fittingSize`](../../nsview/fittingsize.md) message to a view, the smallest size that is large enough for the view’s contents is computed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority-swift.struct/defaultlow)*