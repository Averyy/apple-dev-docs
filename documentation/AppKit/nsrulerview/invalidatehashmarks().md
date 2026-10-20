# invalidateHashMarks()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Forces recalculation of the hash mark spacing for the next time the receiver is displayed.

**Availability**:
- macOS

## Declaration

```swift
func invalidateHashMarks()
```

```objc
- (void) invalidateHashMarks;
```

#### Discussion

You should never need to invoke this method directly, but might need to override it if you override [`drawHashMarksAndLabels(in:)`](./drawhashmarksandlabels%28in%29.md).

## See Also

### Drawing
- [func drawHashMarksAndLabels(in: NSRect)](./drawhashmarksandlabels%28in%29.md)
  Draws the receiver’s hash marks and labels in `aRect`, which is expressed in the receiver’s coordinate system.
- [func drawMarkers(in: NSRect)](./drawmarkers%28in%29.md)
  Draws the receiver’s markers in `aRect`, which is expressed in the receiver’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/invalidatehashmarks())*