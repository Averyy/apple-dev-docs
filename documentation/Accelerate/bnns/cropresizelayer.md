# BNNS.CropResizeLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a crop-resize filter and manages its deinitialization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+
- Unknown ?+ - Deprecated
- tvOS 16.0+

## Declaration

```swift
class CropResizeLayer
```

## Topics

### Creating a Crop-Resize Layer
- [init(coordinatesAreNormalized: Bool, spatialScale: Float, extrapolationValue: Float, samplingMode: BNNS.CropResizeLayer.LinearSamplingMode, boxCoordinateMode: BNNS.CropResizeLayer.BoxCoordinateMode)](bnns/cropresizelayer/init(coordinatesarenormalized:spatialscale:extrapolationvalue:samplingmode:boxcoordinatemode:).md)
  Returns a new crop-resize layer.
### Applying a Crop-Resize Layer
- [func apply(input: BNNSNDArrayDescriptor, regionOfInterest: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/cropresizelayer/apply(input:regionofinterest:output:filterparameters:).md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
- [func applyBackward(regionOfInterest: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/cropresizelayer/applybackward(regionofinterest:outputgradient:generatinginputgradient:filterparameters:).md)
  Applies a crop-resize filter backward to generate an input gradient.
### Suporting Types
- [BNNS.CropResizeLayer.BoxCoordinateMode](bnns/cropresizelayer/boxcoordinatemode.md)
  An enumeration that defines the convention for specifying the bounding box coordinates of a 2D image.
- [BNNS.CropResizeLayer.LinearSamplingMode](bnns/cropresizelayer/linearsamplingmode.md)
  An enumeration that specifies the interpolation sampling mode.

## See Also

- [func BNNSCropResize(UnsafePointer<BNNSLayerParametersCropResize>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresize(_:_:_:_:_:).md)
  Extracts and resizes regions of interest of an input tensor.
- [func BNNSCropResizeBackward(UnsafePointer<BNNSLayerParametersCropResize>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresizebackward(_:_:_:_:_:).md)
  Applies a crop-resize filter backward to generate gradients.
- [struct BNNSLayerParametersCropResize](bnnslayerparameterscropresize.md)
  A set of parameters that describe a crop-resize operation.
- [struct BNNSBoxCoordinateMode](bnnsboxcoordinatemode.md)
  Constants that define the convention to specify the four bounding box coordinates for crop-resize operations.
- [struct BNNSLinearSamplingMode](bnnslinearsamplingmode.md)
  Constants that specify how a crop-resize layer samples a grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/cropresizelayer)*