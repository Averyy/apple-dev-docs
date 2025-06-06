# drawHashMarksAndLabels(in:)

**Framework**: AppKit  
**Kind**: method

Draws the receiver’s hash marks and labels in `aRect`, which is expressed in the receiver’s coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawHashMarksAndLabels(in rect: NSRect)
```

#### Discussion

This method is invoked by [`draw(_:)`](nsrulermarker/draw(_:).md)—you should never need to invoke it directly. You can define custom measurement units using the class method [`registerUnit(withName:abbreviation:unitToPointsConversionFactor:stepUpCycle:stepDownCycle:)`](nsrulerview/registerunit(withname:abbreviation:unittopointsconversionfactor:stepupcycle:stepdowncycle:).md). Override this method if you want to customize the appearance of the hash marks themselves.

## See Also

- [func drawMarkers(in: NSRect)](nsrulerview/drawmarkers(in:).md)
  Draws the receiver’s markers in `aRect`, which is expressed in the receiver’s coordinate system.
- [func invalidateHashMarks()](nsrulerview/invalidatehashmarks.md)
  Forces recalculation of the hash mark spacing for the next time the receiver is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/drawhashmarksandlabels(in:))*