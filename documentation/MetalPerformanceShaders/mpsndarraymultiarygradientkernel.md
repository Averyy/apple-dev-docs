# MPSNDArrayMultiaryGradientKernel

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
class MPSNDArrayMultiaryGradientKernel
```

```objc
@interface MPSNDArrayMultiaryGradientKernel : MPSNDArrayMultiaryBase
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](./mpsndarraymultiarygradientkernel/init%28coder,device%29.md)
- [init(device: any MTLDevice, sourceCount: Int, sourceGradientIndex: Int)](./mpsndarraymultiarygradientkernel/init%28device,sourcecount,sourcegradientindex%29.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](./mpsndarraymultiarygradientkernel/encode%28to,sourcearrays,sourcegradient,gradientstate%29.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](./mpsndarraymultiarygradientkernel/encode%28to,sourcearrays,sourcegradient,gradientstate,destinationarray%29.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryBase](./mpsndarraymultiarybase.md)
### Inherited By
- [MPSNDArrayBinaryPrimaryGradientKernel](./mpsndarraybinaryprimarygradientkernel.md)
- [MPSNDArrayBinarySecondaryGradientKernel](./mpsndarraybinarysecondarygradientkernel.md)
- [MPSNDArrayUnaryGradientKernel](./mpsndarrayunarygradientkernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarygradientkernel)*