# invalidateHashMarks()

**Framework**: AppKit  
**Kind**: method

Forces recalculation of the hash mark spacing for the next time the receiver is displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func invalidateHashMarks()
```

#### Discussion

You should never need to invoke this method directly, but might need to override it if you override [`drawHashMarksAndLabels(in:)`](nsrulerview/drawhashmarksandlabels(in:).md).

## See Also

- [func drawHashMarksAndLabels(in: NSRect)](nsrulerview/drawhashmarksandlabels(in:).md)
  Draws the receiver’s hash marks and labels in `aRect`, which is expressed in the receiver’s coordinate system.
- [func drawMarkers(in: NSRect)](nsrulerview/drawmarkers(in:).md)
  Draws the receiver’s markers in `aRect`, which is expressed in the receiver’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/invalidatehashmarks())*