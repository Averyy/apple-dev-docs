# sizeToFit()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Resizes the receiver’s frame so that it’s the minimum size needed to contain its cell.

**Availability**:
- macOS

## Declaration

```swift
func sizeToFit()
```

```objc
- (void) sizeToFit;
```

#### Discussion

If you want a multiple-cell custom subclass of `NSControl` to size itself to fit its cells, you must override this method. This method neither redisplays the receiver nor marks it as needing display. You must do this yourself with either the[`display()`](../nsview/display%28%29.md) or [`setNeedsDisplay()`](./setneedsdisplay%28%29.md) method.

## See Also

### Related Documentation
- [func calcSize()](./calcsize%28%29.md)
  Recomputes any internal sizing information for the receiver, if necessary.
### Resizing the Control
- [var controlSize: NSControl.ControlSize](./controlsize-swift.property.md)
  The size of the control.
- [NSControl.ControlSize](./controlsize-swift.enum.md)
  A constant for specifying a cell’s size.
- [func sizeThatFits(NSSize) -> NSSize](./sizethatfits%28_%29.md)
  Asks the control to calculate and return the size that best fits the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/sizetofit())*