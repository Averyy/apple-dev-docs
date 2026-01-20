# MPSNDArrayMultiaryGradientKernel

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
class MPSNDArrayMultiaryGradientKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraymultiarygradientkernel/init(coder:device:).md)
- [init(device: any MTLDevice, sourceCount: Int, sourceGradientIndex: Int)](mpsndarraymultiarygradientkernel/init(device:sourcecount:sourcegradientindex:).md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](mpsndarraymultiarygradientkernel/encode(to:sourcearrays:sourcegradient:gradientstate:).md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](mpsndarraymultiarygradientkernel/encode(to:sourcearrays:sourcegradient:gradientstate:destinationarray:).md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryBase](mpsndarraymultiarybase.md)
### Inherited By
- [MPSNDArrayBinaryPrimaryGradientKernel](mpsndarraybinaryprimarygradientkernel.md)
- [MPSNDArrayBinarySecondaryGradientKernel](mpsndarraybinarysecondarygradientkernel.md)
- [MPSNDArrayUnaryGradientKernel](mpsndarrayunarygradientkernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarygradientkernel)*