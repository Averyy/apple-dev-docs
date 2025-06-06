# object_minimum_iou

**Framework**: Accelerate  
**Kind**: property

The value that specifies intersection over union (IOU) that’s the minimum the function treats as an object.

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
var object_minimum_iou: Float
```

## See Also

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
- [var no_object_maximum_iou: Float](bnnslayerparameterslossyolo/no_object_maximum_iou.md)
  The value that specifies intersection over union (IOU) that’s the maximum the function treats as not an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslossyolo/object_minimum_iou)*