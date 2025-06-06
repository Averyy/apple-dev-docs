# sizeThatFits(_:)

**Framework**: AppKit  
**Kind**: method

Asks the control to calculate and return the size that best fits the specified size.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func sizeThatFits(_ size: NSSize) -> NSSize
```

#### Return Value

A new size that fits the receiver’s subviews.

#### Discussion

By default, this method returns the [`intrinsicContentSize`](nsview/intrinsiccontentsize.md) of the receiver.

## Parameters

- `size`: The size for which the control should calculate its best-fitting size.

## See Also

- [var controlSize: NSControl.ControlSize](nscontrol/controlsize-swift.property.md)
  The size of the control.
- [NSControl.ControlSize](nscontrol/controlsize-swift.enum.md)
  A constant for specifying a cell’s size.
- [func sizeToFit()](nscontrol/sizetofit.md)
  Resizes the receiver’s frame so that it’s the minimum size needed to contain its cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/sizethatfits(_:))*