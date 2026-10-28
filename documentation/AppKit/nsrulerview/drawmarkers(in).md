# drawMarkers(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the receiver’s markers in `aRect`, which is expressed in the receiver’s coordinate system.

**Availability**:
- macOS

## Declaration

```swift
func drawMarkers(in rect: NSRect)
```

```objc
- (void) drawMarkersInRect:(NSRect) rect;
```

## Discussion

This method is invoked by [`draw(_:)`](../nsrulermarker/draw%28_%29.md); you should never need to invoke it directly, but you might want to override it if you want to do something different when drawing markers.

## See Also

### Related Documentation
- [var reservedThicknessForMarkers: CGFloat](./reservedthicknessformarkers.md)
  The room available for ruler markers to `thickness`.
### Drawing
- [func drawHashMarksAndLabels(in: NSRect)](./drawhashmarksandlabels%28in%29.md)
  Draws the receiver’s hash marks and labels in `aRect`, which is expressed in the receiver’s coordinate system.
- [func invalidateHashMarks()](./invalidatehashmarks%28%29.md)
  Forces recalculation of the hash mark spacing for the next time the receiver is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/drawmarkers(in:))*