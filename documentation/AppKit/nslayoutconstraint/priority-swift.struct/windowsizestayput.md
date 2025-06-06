# windowSizeStayPut

**Framework**: AppKit  
**Kind**: property

Priority level for the window’s current size.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let windowSizeStayPut: NSLayoutConstraint.Priority
```

#### Discussion

It’s generally not appropriate to make a constraint at exactly this priority. You want to be higher or lower. Constraints with higher priorities can adjust the window’s size. Constraints with lower priorities must be fulfilled using the current window size.

## See Also

- [static let required: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/required.md)
  A required constraint.
- [static let defaultHigh: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/defaulthigh.md)
  Priority level with which a button resists compressing its content.
- [static let dragThatCanResizeWindow: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/dragthatcanresizewindow.md)
  Appropriate priority level for a drag that may end up resizing the window.
- [static let dragThatCannotResizeWindow: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/dragthatcannotresizewindow.md)
  Priority level at which a split view divider, say, is dragged.
- [static let defaultLow: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/defaultlow.md)
  Priority level at which a button hugs its contents horizontally.
- [static let fittingSizeCompression: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/fittingsizecompression.md)
  When you send a [`fittingSize`](nsview/fittingsize.md) message to a view, the smallest size that is large enough for the view’s contents is computed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority-swift.struct/windowsizestayput)*