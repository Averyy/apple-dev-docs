# BNNSBoxCoordinateMode

**Framework**: Accelerate  
**Kind**: struct

Constants that define the convention to specify the four bounding box coordinates for crop-resize operations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSBoxCoordinateMode
```

## Topics

### Constants
- [init(UInt32)](bnnsboxcoordinatemode/init(_:).md)
- [init(rawValue: UInt32)](bnnsboxcoordinatemode/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsboxcoordinatemode/rawvalue.md)
- [var BNNSCenterSizeHeightFirst: BNNSBoxCoordinateMode](bnnscentersizeheightfirst.md)
  Specifies coordinates as corners with the order: height start, width start, height end, width end.
- [var BNNSCenterSizeWidthFirst: BNNSBoxCoordinateMode](bnnscentersizewidthfirst.md)
  Specifies coordinates as corners with the order: width start, height start, width end, height end.
- [var BNNSCornersHeightFirst: BNNSBoxCoordinateMode](bnnscornersheightfirst.md)
  Specifies coordinates as center and size with the order: height center, width center, height, width.
- [var BNNSCornersWidthFirst: BNNSBoxCoordinateMode](bnnscornerswidthfirst.md)
  Specifies coordinates as center and size with the order: width center, height center, width, height.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CropResizeLayer](bnns/cropresizelayer.md)
  A layer object that wraps a crop-resize filter and manages its deinitialization.
- [func BNNSCropResize(UnsafePointer<BNNSLayerParametersCropResize>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresize(_:_:_:_:_:).md)
  Extracts and resizes regions of interest of an input tensor.
- [func BNNSCropResizeBackward(UnsafePointer<BNNSLayerParametersCropResize>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresizebackward(_:_:_:_:_:).md)
  Applies a crop-resize filter backward to generate gradients.
- [struct BNNSLayerParametersCropResize](bnnslayerparameterscropresize.md)
  A set of parameters that describe a crop-resize operation.
- [struct BNNSLinearSamplingMode](bnnslinearsamplingmode.md)
  Constants that specify how a crop-resize layer samples a grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsboxcoordinatemode)*