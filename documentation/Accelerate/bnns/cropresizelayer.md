# BNNS.CropResizeLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A layer object that wraps a crop-resize filter and manages its deinitialization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
class CropResizeLayer
```

## Topics

### Creating a Crop-Resize Layer
- [init(coordinatesAreNormalized: Bool, spatialScale: Float, extrapolationValue: Float, samplingMode: BNNS.CropResizeLayer.LinearSamplingMode, boxCoordinateMode: BNNS.CropResizeLayer.BoxCoordinateMode)](./cropresizelayer/init%28coordinatesarenormalized,spatialscale,extrapolationvalue,samplingmode,boxcoordinatemode%29.md)
  Returns a new crop-resize layer.
### Applying a Crop-Resize Layer
- [func apply(input: BNNSNDArrayDescriptor, regionOfInterest: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](./cropresizelayer/apply%28input,regionofinterest,output,filterparameters%29.md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.
- [func applyBackward(regionOfInterest: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](./cropresizelayer/applybackward%28regionofinterest,outputgradient,generatinginputgradient,filterparameters%29.md)
  Applies a crop-resize filter backward to generate an input gradient.
### Suporting Types
- [BNNS.CropResizeLayer.BoxCoordinateMode](./cropresizelayer/boxcoordinatemode.md)
  An enumeration that defines the convention for specifying the bounding box coordinates of a 2D image.
- [BNNS.CropResizeLayer.LinearSamplingMode](./cropresizelayer/linearsamplingmode.md)
  An enumeration that specifies the interpolation sampling mode.

## See Also

### Crop-resize layers
- [func BNNSCropResize(UnsafePointer<BNNSLayerParametersCropResize>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnscropresize%28_,_,_,_,_%29.md)
  Extracts and resizes regions of interest of an input tensor.
- [func BNNSCropResizeBackward(UnsafePointer<BNNSLayerParametersCropResize>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnscropresizebackward%28_,_,_,_,_%29.md)
  Applies a crop-resize filter backward to generate gradients.
- [struct BNNSLayerParametersCropResize](../bnnslayerparameterscropresize.md)
  A set of parameters that describe a crop-resize operation.
- [struct BNNSBoxCoordinateMode](../bnnsboxcoordinatemode.md)
  Constants that define the convention to specify the four bounding box coordinates for crop-resize operations.
- [struct BNNSLinearSamplingMode](../bnnslinearsamplingmode.md)
  Constants that specify how a crop-resize layer samples a grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/cropresizelayer)*