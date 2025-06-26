# BNNS.LossFunction.YoloParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters for You Only Look Once (YOLO) loss computation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
struct YoloParameters
```

## Topics

### Instance Properties
- [let anchorBoxCount: Int](bnns/lossfunction/yoloparameters/anchorboxcount.md)
  The number of anchor boxes in each cell.
- [let anchorBoxSize: Int](bnns/lossfunction/yoloparameters/anchorboxsize.md)
  The size of the anchor box.
- [let anchorsData: UnsafeMutablePointer<Float>](bnns/lossfunction/yoloparameters/anchorsdata.md)
  Maximum IOU for treating as no object.
- [let classificationScale: Float](bnns/lossfunction/yoloparameters/classificationscale.md)
  The value that specifies the classification scaling factor.
- [let gridColumnCount: Int](bnns/lossfunction/yoloparameters/gridcolumncount.md)
  The number of columns in the grid.
- [let gridRowsCount: Int](bnns/lossfunction/yoloparameters/gridrowscount.md)
  The number of rows in the grid.
- [let huberDelta: Float](bnns/lossfunction/yoloparameters/huberdelta.md)
  A value that’s interpreted as width-height loss.
- [let noObjectMaximumIoU: Float](bnns/lossfunction/yoloparameters/noobjectmaximumiou.md)
  The value that specifies intersection over union (IOU) that’s the maximum the function treats as not an object.
- [let noObjectScale: Float](bnns/lossfunction/yoloparameters/noobjectscale.md)
  The value that specifies the no-object confidence scaling factor.
- [let objectMinimumIoU: Float](bnns/lossfunction/yoloparameters/objectminimumiou.md)
  The value that specifies intersection over union (IOU) that’s the minimum the function treats as an object.
- [let objectScale: Float](bnns/lossfunction/yoloparameters/objectscale.md)
  The value that specifies the object confidence loss-scaling factor.
- [let rescore: Bool](bnns/lossfunction/yoloparameters/rescore.md)
  A Boolean value that determines whether to rescore confidence according to prediction verus ground truth Intersection Over Union (IOU).
- [let whScale: Float](bnns/lossfunction/yoloparameters/whscale.md)
  A Boolean value that determines whether to rescore confidence according to prediction verus ground truth Intersection Over Union (IOU).
- [let xyScale: Float](bnns/lossfunction/yoloparameters/xyscale.md)
  The value that specifies the x, y loss-scaling factor.
### Initializers
- [init(huberDelta: Float, gridColumnCount: Int, gridRowsCount: Int, anchorBoxCount: Int, anchorBoxSize: Int, rescore: Bool, xyScale: Float, whScale: Float, objectScale: Float, noObjectScale: Float, classificationScale: Float, objectMinimumIoU: Float, noObjectMaximumIoU: Float, anchorsData: UnsafeMutablePointer<Float>)](bnns/lossfunction/yoloparameters/init(huberdelta:gridcolumncount:gridrowscount:anchorboxcount:anchorboxsize:rescore:xyscale:whscale:objectscale:noobjectscale:classificationscale:objectminimumiou:noobjectmaximumiou:anchorsdata:).md)

## See Also

- [BNNS.LossFunction.categoricalCrossEntropy](bnns/lossfunction/categoricalcrossentropy.md)
  Categorical cross-entropy computation between input prediction and labels.
- [BNNS.LossFunction.cosineDistance](bnns/lossfunction/cosinedistance.md)
  Cosine distance loss computation between input predictions and labels.
- [BNNS.LossFunction.hinge](bnns/lossfunction/hinge.md)
  Hinge loss computation between labels and unbounded, zero-centered binary predictions.
- [BNNS.LossFunction.huber(huberDelta:)](bnns/lossfunction/huber(huberdelta:).md)
  Huber loss computation between input logits and one-hot encoded labels.
- [BNNS.LossFunction.log](bnns/lossfunction/log.md)
  Log loss computation between labels and predictions.
- [BNNS.LossFunction.meanAbsoluteError](bnns/lossfunction/meanabsoluteerror.md)
  Mean absolute error (MAE) computation between input prediction and labels.
- [BNNS.LossFunction.meanSquareError](bnns/lossfunction/meansquareerror.md)
  Mean square error (MSE) computation between input logits and one-hot encoded labels.
- [BNNS.LossFunction.sigmoidCrossEntropy(labelSmoothing:)](bnns/lossfunction/sigmoidcrossentropy(labelsmoothing:).md)
  Sigmoid activation on input logits, and independent computation of cross-entropy loss for each class.
- [BNNS.LossFunction.softmaxCrossEntropy(labelSmoothing:)](bnns/lossfunction/softmaxcrossentropy(labelsmoothing:).md)
  Softmax activation on input logits, and computation of cross-entropy loss with one-hot encoded labels.
- [case yolo(parameters: BNNS.LossFunction.YoloParameters)](bnns/lossfunction/yolo(parameters:).md)
  You Only Look Once (YOLO) loss computation between prediction and ground truth labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossfunction/yoloparameters)*