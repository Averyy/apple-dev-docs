# scaleNoObjectConfidenceLoss

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The scale factor you use for no object confidence loss and loss gradient.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var scaleNoObjectConfidenceLoss: Float { get set }
```

```objc
@property (nonatomic, readwrite) float scaleNoObjectConfidenceLoss;
```

## Discussion

The default value is `5.0`.

## See Also

### Inspecting YOLO Loss Descriptors
- [var anchorBoxCount: Int](./anchorboxcount.md)
  The number of anchor boxes you use to detect an object in each grid cell.
- [var anchorBoxes: Data](./anchorboxes.md)
  Data that contains the width and height for all the anchor boxes.
- [var maximumIOUForObjectAbsence: Float](./maximumiouforobjectabsence.md)
  The negative intersection over union (IOU).
- [var minimumIOUForObjectPresence: Float](./minimumiouforobjectpresence.md)
  The positive intersection over union (IOU).
- [var scaleClassLoss: Float](./scaleclassloss.md)
  The scale factor you use for loss when there are no object classes, and for loss gradient.
- [var scaleObjectConfidenceLoss: Float](./scaleobjectconfidenceloss.md)
  The scale factor you use for object confidence loss and loss gradient.
- [var scaleSpatialPositionLoss: Float](./scalespatialpositionloss.md)
  The scale factor you use for spatial position loss and loss gradient.
- [var scaleSpatialSizeLoss: Float](./scalespatialsizeloss.md)
  The scale factor you use for spatial size loss and loss gradient.
- [var shouldRescore: Bool](./shouldrescore.md)
  A Boolean that indicates whether the layer scales the object confidence loss by the intersection over union (IOU) overlap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcyololossdescriptor/scalenoobjectconfidenceloss)*