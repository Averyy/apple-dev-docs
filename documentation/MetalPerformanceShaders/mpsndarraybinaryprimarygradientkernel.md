# MPSNDArrayBinaryPrimaryGradientKernel

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
class MPSNDArrayBinaryPrimaryGradientKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraybinaryprimarygradientkernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsndarraybinaryprimarygradientkernel/init(device:).md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](mpsndarraybinaryprimarygradientkernel/encode(to:primarysourcearray:secondarysourcearray:sourcegradient:gradientstate:).md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](mpsndarraybinaryprimarygradientkernel/encode(to:primarysourcearray:secondarysourcearray:sourcegradient:gradientstate:destinationarray:).md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryGradientKernel](mpsndarraymultiarygradientkernel.md)
### Inherited By
- [MPSNDArrayGatherGradient](mpsndarraygathergradient.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinaryprimarygradientkernel)*