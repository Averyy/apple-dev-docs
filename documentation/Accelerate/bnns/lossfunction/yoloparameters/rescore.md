# rescore

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether to rescore confidence according to prediction verus ground truth Intersection Over Union (IOU).

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
let rescore: Bool
```

## See Also

### Instance Properties
- [let anchorBoxCount: Int](./anchorboxcount.md)
  The number of anchor boxes in each cell.
- [let anchorBoxSize: Int](./anchorboxsize.md)
  The size of the anchor box.
- [let anchorsData: UnsafeMutablePointer<Float>](./anchorsdata.md)
  Maximum IOU for treating as no object.
- [let classificationScale: Float](./classificationscale.md)
  The value that specifies the classification scaling factor.
- [let gridColumnCount: Int](./gridcolumncount.md)
  The number of columns in the grid.
- [let gridRowsCount: Int](./gridrowscount.md)
  The number of rows in the grid.
- [let huberDelta: Float](./huberdelta.md)
  A value that’s interpreted as width-height loss.
- [let noObjectMaximumIoU: Float](./noobjectmaximumiou.md)
  The value that specifies intersection over union (IOU) that’s the maximum the function treats as not an object.
- [let noObjectScale: Float](./noobjectscale.md)
  The value that specifies the no-object confidence scaling factor.
- [let objectMinimumIoU: Float](./objectminimumiou.md)
  The value that specifies intersection over union (IOU) that’s the minimum the function treats as an object.
- [let objectScale: Float](./objectscale.md)
  The value that specifies the object confidence loss-scaling factor.
- [let whScale: Float](./whscale.md)
  A Boolean value that determines whether to rescore confidence according to prediction verus ground truth Intersection Over Union (IOU).
- [let xyScale: Float](./xyscale.md)
  The value that specifies the x, y loss-scaling factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossfunction/yoloparameters/rescore)*