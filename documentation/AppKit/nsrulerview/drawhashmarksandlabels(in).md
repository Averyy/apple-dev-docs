# drawHashMarksAndLabels(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the receiver’s hash marks and labels in `aRect`, which is expressed in the receiver’s coordinate system.

**Availability**:
- macOS

## Declaration

```swift
func drawHashMarksAndLabels(in rect: NSRect)
```

```objc
- (void) drawHashMarksAndLabelsInRect:(NSRect) rect;
```

## Discussion

This method is invoked by [`draw(_:)`](../nsrulermarker/draw%28_%29.md)—you should never need to invoke it directly. You can define custom measurement units using the class method [`registerUnit(withName:abbreviation:unitToPointsConversionFactor:stepUpCycle:stepDownCycle:)`](./registerunit%28withname,abbreviation,unittopointsconversionfactor,stepupcycle,stepdowncycle%29.md). Override this method if you want to customize the appearance of the hash marks themselves.

## See Also

### Drawing
- [func drawMarkers(in: NSRect)](./drawmarkers%28in%29.md)
  Draws the receiver’s markers in `aRect`, which is expressed in the receiver’s coordinate system.
- [func invalidateHashMarks()](./invalidatehashmarks%28%29.md)
  Forces recalculation of the hash mark spacing for the next time the receiver is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/drawhashmarksandlabels(in:))*