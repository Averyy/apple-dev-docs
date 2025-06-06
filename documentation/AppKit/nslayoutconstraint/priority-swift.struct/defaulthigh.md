# defaultHigh

**Framework**: AppKit  
**Kind**: property

Priority level with which a button resists compressing its content.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let defaultHigh: NSLayoutConstraint.Priority
```

#### Discussion

Note that the level is higher than [`windowSizeStayPut`](nslayoutconstraint/priority-swift.struct/windowsizestayput.md). This means dragging to resize a window will not make buttons clip, rather the window frame is constrained.

## See Also

- [static let required: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/required.md)
  A required constraint.
- [static let dragThatCanResizeWindow: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/dragthatcanresizewindow.md)
  Appropriate priority level for a drag that may end up resizing the window.
- [static let windowSizeStayPut: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/windowsizestayput.md)
  Priority level for the window’s current size.
- [static let dragThatCannotResizeWindow: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/dragthatcannotresizewindow.md)
  Priority level at which a split view divider, say, is dragged.
- [static let defaultLow: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/defaultlow.md)
  Priority level at which a button hugs its contents horizontally.
- [static let fittingSizeCompression: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/fittingsizecompression.md)
  When you send a [`fittingSize`](nsview/fittingsize.md) message to a view, the smallest size that is large enough for the view’s contents is computed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority-swift.struct/defaulthigh)*