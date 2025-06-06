# drawMarkers(in:)

**Framework**: AppKit  
**Kind**: method

Draws the receiver’s markers in `aRect`, which is expressed in the receiver’s coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawMarkers(in rect: NSRect)
```

#### Discussion

This method is invoked by [`draw(_:)`](nsrulermarker/draw(_:).md); you should never need to invoke it directly, but you might want to override it if you want to do something different when drawing markers.

## See Also

- [var reservedThicknessForMarkers: CGFloat](nsrulerview/reservedthicknessformarkers.md)
  The room available for ruler markers to `thickness`.
- [func drawHashMarksAndLabels(in: NSRect)](nsrulerview/drawhashmarksandlabels(in:).md)
  Draws the receiver’s hash marks and labels in `aRect`, which is expressed in the receiver’s coordinate system.
- [func invalidateHashMarks()](nsrulerview/invalidatehashmarks.md)
  Forces recalculation of the hash mark spacing for the next time the receiver is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/drawmarkers(in:))*