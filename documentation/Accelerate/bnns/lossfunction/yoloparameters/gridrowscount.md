# gridRowsCount

**Framework**: Accelerate  
**Kind**: property

The number of rows in the grid.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
let gridRowsCount: Int
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossfunction/yoloparameters/gridrowscount)*