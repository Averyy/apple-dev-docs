# init(function:i_desc:o_desc:reduction:huber_delta:number_of_grid_columns:number_of_grid_rows:number_of_anchor_boxes:anchor_box_size:rescore:scale_xy:scale_wh:scale_object:scale_no_object:scale_classification:object_minimum_iou:no_object_maximum_iou:anchors_data:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new You Only Look Once (YOLO) loss layer parameters structure from the specified parameters.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
init(function: BNNSLossFunction, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, reduction: BNNSLossReductionFunction, huber_delta: Float, number_of_grid_columns: Int, number_of_grid_rows: Int, number_of_anchor_boxes: Int, anchor_box_size: Int, rescore: Bool, scale_xy: Float, scale_wh: Float, scale_object: Float, scale_no_object: Float, scale_classification: Float, object_minimum_iou: Float, no_object_maximum_iou: Float, anchors_data: UnsafeMutablePointer<Float>)
```

#### Discussion

> ❗ **Important**:  The input data type and output data type must be `float`. The output size must be `1`, unless the reduction is [`BNNS.LossReduction.none`](../bnns/lossreduction/none.md).

## Parameters

- `function`: The function that’s used to compute loss.
- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `reduction`: The function that’s used to reduce the computed loss (must be sum reduction for YOLO).
- `huber_delta`: A value that’s interpreted as width-height loss.
- `number_of_grid_columns`: The number of columns in the grid.
- `number_of_grid_rows`: The number of rows in the grid.
- `number_of_anchor_boxes`: The number of anchor boxes in each cell.
- `anchor_box_size`: The size of the anchor box.
- `rescore`: A Boolean value that determines whether to rescore confidence according to prediction verus ground truth Intersection Over Union (IOU).
- `scale_xy`: The value that specifies the x, y loss-scaling factor.
- `scale_wh`: The value that specifies the w, h loss-scaling factor.
- `scale_object`: The value that specifies the object confidence loss-scaling factor.
- `scale_no_object`: The value that specifies the no-object confidence scaling factor.
- `scale_classification`: The value that specifies the classification scaling factor.
- `object_minimum_iou`: The value that specifies intersection over union (IOU) that’s the minimum the function treats as an object.
- `no_object_maximum_iou`: The value that specifies intersection over union (IOU) that’s the maximum the function treats as not an object.
- `anchors_data`: Anchors data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslossyolo/init(function:i_desc:o_desc:reduction:huber_delta:number_of_grid_columns:number_of_grid_rows:number_of_anchor_boxes:anchor_box_size:rescore:scale_xy:scale_wh:scale_object:scale_no_object:scale_classification:object_minimum_iou:no_object_max-4sykc)*