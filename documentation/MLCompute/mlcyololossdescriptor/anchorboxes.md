# anchorBoxes

**Framework**: ML Compute  
**Kind**: property

Data that contains the width and height for all the anchor boxes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var anchorBoxes: Data { get }
```

#### Discussion

This data has [`anchorBoxCount`](mlcyololossdescriptor/anchorboxcount.md) pairs of floating-point values that represent the width and height of each anchor box.

## See Also

- [var anchorBoxCount: Int](mlcyololossdescriptor/anchorboxcount.md)
  The number of anchor boxes you use to detect an object in each grid cell.
- [var maximumIOUForObjectAbsence: Float](mlcyololossdescriptor/maximumiouforobjectabsence.md)
  The negative intersection over union (IOU).
- [var minimumIOUForObjectPresence: Float](mlcyololossdescriptor/minimumiouforobjectpresence.md)
  The positive intersection over union (IOU).
- [var scaleClassLoss: Float](mlcyololossdescriptor/scaleclassloss.md)
  The scale factor you use for loss when there are no object classes, and for loss gradient.
- [var scaleObjectConfidenceLoss: Float](mlcyololossdescriptor/scaleobjectconfidenceloss.md)
  The scale factor you use for object confidence loss and loss gradient.
- [var scaleNoObjectConfidenceLoss: Float](mlcyololossdescriptor/scalenoobjectconfidenceloss.md)
  The scale factor you use for no object confidence loss and loss gradient.
- [var scaleSpatialPositionLoss: Float](mlcyololossdescriptor/scalespatialpositionloss.md)
  The scale factor you use for spatial position loss and loss gradient.
- [var scaleSpatialSizeLoss: Float](mlcyololossdescriptor/scalespatialsizeloss.md)
  The scale factor you use for spatial size loss and loss gradient.
- [var shouldRescore: Bool](mlcyololossdescriptor/shouldrescore.md)
  A Boolean that indicates whether the layer scales the object confidence loss by the intersection over union (IOU) overlap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcyololossdescriptor/anchorboxes)*