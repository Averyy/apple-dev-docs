# MLCYOLOLossDescriptor

**Framework**: ML Compute  
**Kind**: class

The configuration object you use to create the YOLO loss layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCYOLOLossDescriptor
```

## Topics

### Creating YOLO Loss Descriptors
- [convenience init(anchorBoxes: Data, anchorBoxCount: Int)](mlcyololossdescriptor/init(anchorboxes:anchorboxcount:).md)
  Creates a YOLO loss filter descriptor with the anchor box data and number of anchor boxes you specify.
### Inspecting YOLO Loss Descriptors
- [var anchorBoxCount: Int](mlcyololossdescriptor/anchorboxcount.md)
  The number of anchor boxes you use to detect an object in each grid cell.
- [var anchorBoxes: Data](mlcyololossdescriptor/anchorboxes.md)
  Data that contains the width and height for all the anchor boxes.
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(descriptor: MLCYOLOLossDescriptor)](mlcyololosslayer/init(descriptor:).md)
  Creates a YOLO loss layer with the descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcyololossdescriptor)*