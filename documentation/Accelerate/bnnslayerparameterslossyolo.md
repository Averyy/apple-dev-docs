# BNNSLayerParametersLossYolo

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a You Only Look Once (YOLO) loss layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct BNNSLayerParametersLossYolo
```

## Topics

### Initializers
- [init(function: BNNSLossFunction, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, reduction: BNNSLossReductionFunction, huber_delta: Float, number_of_grid_columns: Int, number_of_grid_rows: Int, number_of_anchor_boxes: Int, anchor_box_size: Int, rescore: Bool, scale_xy: Float, scale_wh: Float, scale_object: Float, scale_no_object: Float, scale_classification: Float, object_minimum_iou: Float, no_object_maximum_iou: Float, anchors_data: UnsafeMutablePointer<Float>)](bnnslayerparameterslossyolo/init(function:i_desc:o_desc:reduction:huber_delta:number_of_grid_columns:number_of_grid_rows:number_of_anchor_boxes:anchor_box_size:rescore:scale_xy:scale_wh:scale_object:scale_no_object:scale_classification:object_minimum_iou:no_object_max-4sykc.md)
  Returns a new You Only Look Once (YOLO) loss layer parameters structure from the specified parameters.
### Instance Properties
- [var function: BNNSLossFunction](bnnslayerparameterslossyolo/function.md)
  The function that’s used to compute loss.
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparameterslossyolo/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparameterslossyolo/o_desc.md)
  The descriptor of the output.
- [var reduction: BNNSLossReductionFunction](bnnslayerparameterslossyolo/reduction.md)
  The function that’s used to reduce the computed loss (must be sum reduction for YOLO).
- [var huber_delta: Float](bnnslayerparameterslossyolo/huber_delta.md)
  A value that’s interpreted as width-height loss.
- [var number_of_grid_columns: Int](bnnslayerparameterslossyolo/number_of_grid_columns.md)
  The number of columns in the grid.
- [var number_of_grid_rows: Int](bnnslayerparameterslossyolo/number_of_grid_rows.md)
  The number of rows in the grid.
- [var number_of_anchor_boxes: Int](bnnslayerparameterslossyolo/number_of_anchor_boxes.md)
  The number of anchor boxes in each cell.
- [var anchor_box_size: Int](bnnslayerparameterslossyolo/anchor_box_size.md)
  The size of the anchor box.
- [var rescore: Bool](bnnslayerparameterslossyolo/rescore.md)
  A Boolean value that determines whether to rescore confidence according to prediction verus ground truth Intersection Over Union (IOU).
- [var scale_xy: Float](bnnslayerparameterslossyolo/scale_xy.md)
  The value that specifies the x, y loss-scaling factor.
- [var scale_wh: Float](bnnslayerparameterslossyolo/scale_wh.md)
  A Boolean value that determines whether to rescore confidence according to prediction verus ground truth Intersection Over Union (IOU).
- [var scale_object: Float](bnnslayerparameterslossyolo/scale_object.md)
  The value that specifies the object confidence loss-scaling factor.
- [var scale_no_object: Float](bnnslayerparameterslossyolo/scale_no_object.md)
  The value that specifies the no-object confidence scaling factor.
- [var object_minimum_iou: Float](bnnslayerparameterslossyolo/object_minimum_iou.md)
  The value that specifies intersection over union (IOU) that’s the minimum the function treats as an object.
- [var no_object_maximum_iou: Float](bnnslayerparameterslossyolo/no_object_maximum_iou.md)
  The value that specifies intersection over union (IOU) that’s the maximum the function treats as not an object.
- [var scale_classification: Float](bnnslayerparameterslossyolo/scale_classification.md)
  The value that specifies the classification scaling factor.
- [var anchors_data: UnsafeMutablePointer<Float>](bnnslayerparameterslossyolo/anchors_data.md)
  Maximum IOU for treating as no object.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class LossLayer](bnns/losslayer.md)
  A layer object that wraps a loss filter and manages its deinitialization.
- [struct BNNSLossFunction](bnnslossfunction.md)
  Constants that describe loss functions.
- [struct BNNSLossReductionFunction](bnnslossreductionfunction.md)
  Constants that describe reduction functions used by a loss layer.
- [struct BNNSLayerParametersLossBase](bnnslayerparameterslossbase.md)
  A structure that contains the parameters of a loss layer.
- [struct BNNSLayerParametersLossHuber](bnnslayerparameterslosshuber.md)
  A structure that contains the parameters of a Huber loss layer.
- [struct BNNSLayerParametersLossSigmoidCrossEntropy](bnnslayerparameterslosssigmoidcrossentropy.md)
  A structure that contains the parameters of a sigmoid cross entropy loss layer.
- [struct BNNSLayerParametersLossSoftmaxCrossEntropy](bnnslayerparameterslosssoftmaxcrossentropy.md)
  A structure that contains the parameters of a softmax cross entropy loss layer.
- [func BNNSFilterCreateLayerLoss(UnsafeRawPointer, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerloss(_:_:).md)
  Returns a new loss layer.
- [func BNNSLossFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafeMutableRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int) -> Int32](bnnslossfilterapplybatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a loss filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSLossFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnslossfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a loss filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslossyolo)*