# MPSNDArrayBinarySecondaryGradientKernel

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNDArrayBinarySecondaryGradientKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraybinarysecondarygradientkernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsndarraybinarysecondarygradientkernel/init(device:).md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](mpsndarraybinarysecondarygradientkernel/encode(to:primarysourcearray:secondarysourcearray:sourcegradient:gradientstate:).md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](mpsndarraybinarysecondarygradientkernel/encode(to:primarysourcearray:secondarysourcearray:sourcegradient:gradientstate:destinationarray:).md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryGradientKernel](mpsndarraymultiarygradientkernel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinarysecondarygradientkernel)*