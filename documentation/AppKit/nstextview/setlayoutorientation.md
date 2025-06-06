# setLayoutOrientation(_:)

**Framework**: AppKit  
**Kind**: method

Changes the receiver’s layout orientation and invalidates the contents.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func setLayoutOrientation(_ orientation: NSLayoutManager.TextLayoutOrientation)
```

#### Discussion

Unlike other `NSTextView` properties, this is not shared by sibling views.  It also rotates the bounds 90 degrees, swaps horizontal and vertical bits of the [`autoresizingMask`](nsview/autoresizingmask-swift.property.md) mask, and reconfigures [`isHorizontallyResizable`](nstext/ishorizontallyresizable.md) and [`isVerticallyResizable`](nstext/isverticallyresizable.md) properties accordingly.  Also, if [`enclosingScrollView`](nsview/enclosingscrollview.md) returns non-`nil`, it reconfigures the horizontal and vertical ruler views, the horizontal and vertical scrollers, and the frame.

## Parameters

- `orientation`: The text layout orientation.

## See Also

- [func changeLayoutOrientation(Any?)](nstextview/changelayoutorientation(_:).md)
  An action method that sets the layout orientation of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setlayoutorientation(_:))*