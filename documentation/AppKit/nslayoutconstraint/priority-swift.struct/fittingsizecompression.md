# fittingSizeCompression

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

When you send a [`fittingSize`](../../nsview/fittingsize.md) message to a view, the smallest size that is large enough for the view’s contents is computed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var fittingSizeCompression: NSLayoutConstraint.Priority { get }
```

```c
static const NSLayoutPriority NSLayoutPriorityFittingSizeCompression;
```

#### Discussion

This is the priority level with which the view wants to be as small as possible in that computation. It’s quite low. It is generally not appropriate to make a constraint at exactly this priority. You want to be higher or lower.

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
- [static var defaultLow: NSLayoutConstraint.Priority](./defaultlow.md)
  Priority level at which a button hugs its contents horizontally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority-swift.struct/fittingsizecompression)*