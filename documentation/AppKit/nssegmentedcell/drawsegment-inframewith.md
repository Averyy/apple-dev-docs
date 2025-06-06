# drawSegment(_:inFrame:with:)

**Framework**: AppKit  
**Kind**: method

Draws the image and label of the segment in the specified view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawSegment(_ segment: Int, inFrame frame: NSRect, with controlView: NSView)
```

#### Discussion

You can override this method to provide a custom appearance for segmented controls. You should not call this method directly. It is called for you automatically by the control when it needs to be redrawn.

## Parameters

- `segment`: The index of the segment to draw. This method raises an exception ( ) if the index is out of bounds.
- `frame`: The rectangle in which to draw the segment’s image and label. This rectangle is specified in user space coordinates of the specified view.
- `controlView`: The view that contains the segment.

## See Also

- [func draw(withFrame: NSRect, in: NSView)](nscell/draw(withframe:in:).md)
  Draws the receiver’s border and then draws the interior of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/drawsegment(_:inframe:with:))*