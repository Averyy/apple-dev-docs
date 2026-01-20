# MPSNDArrayUnaryGradientKernel

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
class MPSNDArrayUnaryGradientKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarrayunarygradientkernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsndarrayunarygradientkernel/init(device:).md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](mpsndarrayunarygradientkernel/encode(to:sourcearray:sourcegradient:gradientstate:).md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](mpsndarrayunarygradientkernel/encode(to:sourcearray:sourcegradient:gradientstate:destinationarray:).md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryGradientKernel](mpsndarraymultiarygradientkernel.md)
### Inherited By
- [MPSNDArrayStridedSliceGradient](mpsndarraystridedslicegradient.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarygradientkernel)*