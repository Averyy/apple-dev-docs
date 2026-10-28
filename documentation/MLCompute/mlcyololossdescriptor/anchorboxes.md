# anchorBoxes

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

Data that contains the width and height for all the anchor boxes.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var anchorBoxes: Data { get }
```

```objc
@property (nonatomic, copy, readonly, nonnull) NSData * anchorBoxes;
```

## Discussion

This data has [`anchorBoxCount`](./anchorboxcount.md) pairs of floating-point values that represent the width and height of each anchor box.

## See Also

### Inspecting YOLO Loss Descriptors
- [var anchorBoxCount: Int](./anchorboxcount.md)
  The number of anchor boxes you use to detect an object in each grid cell.
- [var maximumIOUForObjectAbsence: Float](./maximumiouforobjectabsence.md)
  The negative intersection over union (IOU).
- [var minimumIOUForObjectPresence: Float](./minimumiouforobjectpresence.md)
  The positive intersection over union (IOU).
- [var scaleClassLoss: Float](./scaleclassloss.md)
  The scale factor you use for loss when there are no object classes, and for loss gradient.
- [var scaleObjectConfidenceLoss: Float](./scaleobjectconfidenceloss.md)
  The scale factor you use for object confidence loss and loss gradient.
- [var scaleNoObjectConfidenceLoss: Float](./scalenoobjectconfidenceloss.md)
  The scale factor you use for no object confidence loss and loss gradient.
- [var scaleSpatialPositionLoss: Float](./scalespatialpositionloss.md)
  The scale factor you use for spatial position loss and loss gradient.
- [var scaleSpatialSizeLoss: Float](./scalespatialsizeloss.md)
  The scale factor you use for spatial size loss and loss gradient.
- [var shouldRescore: Bool](./shouldrescore.md)
  A Boolean that indicates whether the layer scales the object confidence loss by the intersection over union (IOU) overlap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcyololossdescriptor/anchorboxes)*