# MPSNDArrayBinaryPrimaryGradientKernel

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
class MPSNDArrayBinaryPrimaryGradientKernel
```

```objc
@interface MPSNDArrayBinaryPrimaryGradientKernel : MPSNDArrayMultiaryGradientKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](./mpsndarraybinaryprimarygradientkernel/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsndarraybinaryprimarygradientkernel/init%28device%29.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](./mpsndarraybinaryprimarygradientkernel/encode%28to,primarysourcearray,secondarysourcearray,sourcegradient,gradientstate%29.md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](./mpsndarraybinaryprimarygradientkernel/encode%28to,primarysourcearray,secondarysourcearray,sourcegradient,gradientstate,destinationarray%29.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryGradientKernel](./mpsndarraymultiarygradientkernel.md)
### Inherited By
- [MPSNDArrayGatherGradient](./mpsndarraygathergradient.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinaryprimarygradientkernel)*