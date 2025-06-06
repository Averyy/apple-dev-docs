# sizeToFit()

**Framework**: AppKit  
**Kind**: method

Resizes the receiver’s frame so that it’s the minimum size needed to contain its cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sizeToFit()
```

#### Discussion

If you want a multiple-cell custom subclass of `NSControl` to size itself to fit its cells, you must override this method. This method neither redisplays the receiver nor marks it as needing display. You must do this yourself with either the[`display()`](nsview/display().md) or [`setNeedsDisplay()`](nscontrol/setneedsdisplay().md) method.

## See Also

- [func calcSize()](nscontrol/calcsize.md)
  Recomputes any internal sizing information for the receiver, if necessary.
- [var controlSize: NSControl.ControlSize](nscontrol/controlsize-swift.property.md)
  The size of the control.
- [NSControl.ControlSize](nscontrol/controlsize-swift.enum.md)
  A constant for specifying a cell’s size.
- [func sizeThatFits(NSSize) -> NSSize](nscontrol/sizethatfits(_:).md)
  Asks the control to calculate and return the size that best fits the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/sizetofit())*