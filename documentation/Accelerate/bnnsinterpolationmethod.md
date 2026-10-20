# BNNSInterpolationMethod

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that describe interpolation methods.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSInterpolationMethod
```

```c
typedef enum { ... } BNNSInterpolationMethod;
```

## Topics

### Interpolation Methods
- [var rawValue: UInt32](./bnnsinterpolationmethod/rawvalue.md)
- [init(UInt32)](./bnnsinterpolationmethod/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnsinterpolationmethod/init%28rawvalue%29.md)
- [var BNNSInterpolationMethodLinear: BNNSInterpolationMethod](./bnnsinterpolationmethodlinear.md)
  Interpolation that is linear or bilinear depending on the number of resized dimensions.
- [var BNNSInterpolationMethodNearest: BNNSInterpolationMethod](./bnnsinterpolationmethodnearest.md)
  Nearest-neighbor interpolation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Resize layers
- [class ResizeLayer](./bnns/resizelayer.md)
  A layer object that wraps a resize filter and manages its deinitialization.
- [struct BNNSLayerParametersResize](./bnnslayerparametersresize.md)
  A structure that contains the parameters of a resize layer.
- [func BNNSFilterCreateLayerResize(UnsafePointer<BNNSLayerParametersResize>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerresize%28_,_%29.md)
  Returns a new resize layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsinterpolationmethod)*