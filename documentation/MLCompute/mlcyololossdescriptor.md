# MLCYOLOLossDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

The configuration object you use to create the YOLO loss layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCYOLOLossDescriptor
```

```objc
@interface MLCYOLOLossDescriptor : NSObject
```

## Topics

### Creating YOLO Loss Descriptors
- [convenience init(anchorBoxes: Data, anchorBoxCount: Int)](./mlcyololossdescriptor/init%28anchorboxes,anchorboxcount%29.md)
  Creates a YOLO loss filter descriptor with the anchor box data and number of anchor boxes you specify.
### Inspecting YOLO Loss Descriptors
- [var anchorBoxCount: Int](./mlcyololossdescriptor/anchorboxcount.md)
  The number of anchor boxes you use to detect an object in each grid cell.
- [var anchorBoxes: Data](./mlcyololossdescriptor/anchorboxes.md)
  Data that contains the width and height for all the anchor boxes.
- [var maximumIOUForObjectAbsence: Float](./mlcyololossdescriptor/maximumiouforobjectabsence.md)
  The negative intersection over union (IOU).
- [var minimumIOUForObjectPresence: Float](./mlcyololossdescriptor/minimumiouforobjectpresence.md)
  The positive intersection over union (IOU).
- [var scaleClassLoss: Float](./mlcyololossdescriptor/scaleclassloss.md)
  The scale factor you use for loss when there are no object classes, and for loss gradient.
- [var scaleObjectConfidenceLoss: Float](./mlcyololossdescriptor/scaleobjectconfidenceloss.md)
  The scale factor you use for object confidence loss and loss gradient.
- [var scaleNoObjectConfidenceLoss: Float](./mlcyololossdescriptor/scalenoobjectconfidenceloss.md)
  The scale factor you use for no object confidence loss and loss gradient.
- [var scaleSpatialPositionLoss: Float](./mlcyololossdescriptor/scalespatialpositionloss.md)
  The scale factor you use for spatial position loss and loss gradient.
- [var scaleSpatialSizeLoss: Float](./mlcyololossdescriptor/scalespatialsizeloss.md)
  The scale factor you use for spatial size loss and loss gradient.
- [var shouldRescore: Bool](./mlcyololossdescriptor/shouldrescore.md)
  A Boolean that indicates whether the layer scales the object confidence loss by the intersection over union (IOU) overlap.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating YOLO Loss Layers
- [convenience init(descriptor: MLCYOLOLossDescriptor)](./mlcyololosslayer/init%28descriptor%29.md)
  Creates a YOLO loss layer with the descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcyololossdescriptor)*