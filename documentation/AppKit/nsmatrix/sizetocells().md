# sizeToCells()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Changes the width and the height of the receiver’s frame so it exactly contains the cells.

**Availability**:
- macOS

## Declaration

```swift
func sizeToCells()
```

```objc
- (void) sizeToCells;
```

#### Discussion

This method does not redraw the receiver.

## See Also

### Related Documentation
- [func setFrameSize(NSSize)](../nsview/setframesize%28_%29.md)
  Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [func sizeToFit()](../nscontrol/sizetofit%28%29.md)
  Resizes the receiver’s frame so that it’s the minimum size needed to contain its cell.
### Resizing the Matrix and Its Cells
- [var autosizesCells: Bool](./autosizescells.md)
  A Boolean that indicates whether the cell sizes change when the receiver is resized.
- [func setValidateSize(Bool)](./setvalidatesize%28_%29.md)
  Specifies whether the receiver’s size information is validated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/sizetocells())*