# MPSNDArrayUnaryGradientKernel

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNDArrayUnaryGradientKernel
```

```objc
@interface MPSNDArrayUnaryGradientKernel : MPSNDArrayMultiaryGradientKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](./mpsndarrayunarygradientkernel/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsndarrayunarygradientkernel/init%28device%29.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](./mpsndarrayunarygradientkernel/encode%28to,sourcearray,sourcegradient,gradientstate%29.md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](./mpsndarrayunarygradientkernel/encode%28to,sourcearray,sourcegradient,gradientstate,destinationarray%29.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryGradientKernel](./mpsndarraymultiarygradientkernel.md)
### Inherited By
- [MPSNDArrayStridedSliceGradient](./mpsndarraystridedslicegradient.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarygradientkernel)*