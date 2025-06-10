# BNNS.ResizeLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a resize filter and manages its deinitialization.

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
class ResizeLayer
```

## Topics

### Creating a Resize Layer
- [convenience init?(interpolationMethod: BNNS.InterpolationMethod, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, alignsCorners: Bool, filterParameters: BNNSFilterParameters?)](bnns/resizelayer/init(interpolationmethod:input:output:alignscorners:filterparameters:).md)
  Returns a new resize layer.
### Specifying an Interpolation Method
- [BNNS.InterpolationMethod](bnns/interpolationmethod.md)
  Constants that specify interpolation methods for resize operations.

## Relationships

### Inherits From
- [BNNS.UnaryLayer](bnns/unarylayer.md)

## See Also

- [struct BNNSInterpolationMethod](bnnsinterpolationmethod.md)
  Constants that describe interpolation methods.
- [struct BNNSLayerParametersResize](bnnslayerparametersresize.md)
  A structure that contains the parameters of a resize layer.
- [func BNNSFilterCreateLayerResize(UnsafePointer<BNNSLayerParametersResize>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerresize(_:_:).md)
  Returns a new resize layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/resizelayer)*