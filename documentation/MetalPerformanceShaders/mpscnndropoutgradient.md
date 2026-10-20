# MPSCNNDropoutGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A gradient dropout filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDropoutGradient
```

```objc
@interface MPSCNNDropoutGradient : MPSCNNGradientKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnndropoutgradient/init%28coder,device%29.md)
- [init(device: any MTLDevice, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](./mpscnndropoutgradient/init%28device,keepprobability,seed,maskstrideinpixels%29.md)
### Instance Properties
- [var keepProbability: Float](./mpscnndropoutgradient/keepprobability.md)
- [var maskStrideInPixels: MTLSize](./mpscnndropoutgradient/maskstrideinpixels.md)
- [var seed: Int](./mpscnndropoutgradient/seed.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](./mpscnngradientkernel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Dropout Layers
- [class MPSCNNDropout](./mpscnndropout.md)
  A dropout filter.
- [class MPSCNNDropoutGradientState](./mpscnndropoutgradientstate.md)
  A class that stores the mask used by dropout and gradient dropout filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutgradient)*