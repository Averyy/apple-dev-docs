# sizeToCells()

**Framework**: AppKit  
**Kind**: method

Changes the width and the height of the receiver’s frame so it exactly contains the cells.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sizeToCells()
```

#### Discussion

This method does not redraw the receiver.

## See Also

- [func setFrameSize(NSSize)](nsview/setframesize(_:).md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [func sizeToFit()](nscontrol/sizetofit.md)
  Resizes the receiver’s frame so that it’s the minimum size needed to contain its cell.
- [var autosizesCells: Bool](nsmatrix/autosizescells.md)
  A Boolean that indicates whether the cell sizes change when the receiver is resized.
- [func setValidateSize(Bool)](nsmatrix/setvalidatesize(_:).md)
  Specifies whether the receiver’s size information is validated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/sizetocells())*