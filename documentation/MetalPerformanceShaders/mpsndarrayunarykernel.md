# MPSNDArrayUnaryKernel

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
class MPSNDArrayUnaryKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarrayunarykernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsndarrayunarykernel/init(device:).md)
### Instance Properties
- [var dilationRates: MPSNDArraySizes](mpsndarrayunarykernel/dilationrates.md)
- [var edgeMode: MPSImageEdgeMode](mpsndarrayunarykernel/edgemode.md)
- [var kernelSizes: MPSNDArraySizes](mpsndarrayunarykernel/kernelsizes.md)
- [var offsets: MPSNDArrayOffsets](mpsndarrayunarykernel/offsets.md)
- [var strides: MPSNDArrayOffsets](mpsndarrayunarykernel/strides.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray) -> MPSNDArray](mpsndarrayunarykernel/encode(to:sourcearray:).md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, destinationArray: MPSNDArray)](mpsndarrayunarykernel/encode(to:sourcearray:destinationarray:).md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, resultState: MPSState?, destinationArray: MPSNDArray)](mpsndarrayunarykernel/encode(to:sourcearray:resultstate:destinationarray:).md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](mpsndarrayunarykernel/encode(to:sourcearray:resultstate:outputstateistemporary:).md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryKernel](mpsndarraymultiarykernel.md)
### Inherited By
- [MPSNDArrayIdentity](mpsndarrayidentity.md)
- [MPSNDArrayStridedSlice](mpsndarraystridedslice.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarykernel)*