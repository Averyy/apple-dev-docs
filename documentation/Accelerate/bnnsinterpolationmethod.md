# BNNSInterpolationMethod

**Framework**: Accelerate  
**Kind**: struct

Constants that describe interpolation methods.

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
struct BNNSInterpolationMethod
```

## Topics

### Interpolation Methods
- [var rawValue: UInt32](bnnsinterpolationmethod/rawvalue.md)
- [init(UInt32)](bnnsinterpolationmethod/init(_:).md)
- [init(rawValue: UInt32)](bnnsinterpolationmethod/init(rawvalue:).md)
- [var BNNSInterpolationMethodLinear: BNNSInterpolationMethod](bnnsinterpolationmethodlinear.md)
  Interpolation that is linear or bilinear depending on the number of resized dimensions.
- [var BNNSInterpolationMethodNearest: BNNSInterpolationMethod](bnnsinterpolationmethodnearest.md)
  Nearest-neighbor interpolation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ResizeLayer](bnns/resizelayer.md)
  A layer object that wraps a resize filter and manages its deinitialization.
- [struct BNNSLayerParametersResize](bnnslayerparametersresize.md)
  A structure that contains the parameters of a resize layer.
- [func BNNSFilterCreateLayerResize(UnsafePointer<BNNSLayerParametersResize>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerresize(_:_:).md)
  Returns a new resize layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsinterpolationmethod)*