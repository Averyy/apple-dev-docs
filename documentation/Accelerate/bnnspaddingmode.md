# BNNSPaddingMode

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that define padding modes.

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
struct BNNSPaddingMode
```

```c
typedef enum { ... } BNNSPaddingMode;
```

## Topics

### Padding Modes
- [init(UInt32)](./bnnspaddingmode/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnspaddingmode/init%28rawvalue%29.md)
- [var rawValue: UInt32](./bnnspaddingmode/rawvalue.md)
- [var BNNSPaddingModeConstant: BNNSPaddingMode](./bnnspaddingmodeconstant.md)
  A constant that indicates that a padding operation fills the padded area with a specified constant.
- [var BNNSPaddingModeReflect: BNNSPaddingMode](./bnnspaddingmodereflect.md)
  A constant that indicates that a padding operation fills the padded area to form an odd-symmetric pattern.
- [var BNNSPaddingModeSymmetric: BNNSPaddingMode](./bnnspaddingmodesymmetric.md)
  A constant that indicates that a padding operation fills the padded area to form an even-symmetric pattern.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Padding layers
- [class PaddingLayer](./bnns/paddinglayer.md)
  A layer object that wraps a padding filter and manages its deinitialization.
- [struct BNNSLayerParametersPadding](./bnnslayerparameterspadding.md)
  A structure that contains the parameters of a padding layer.
- [func BNNSFilterCreateLayerPadding(UnsafePointer<BNNSLayerParametersPadding>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerpadding%28_,_%29.md)
  Returns a new loss layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspaddingmode)*