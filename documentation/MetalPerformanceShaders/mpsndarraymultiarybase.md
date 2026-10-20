# MPSNDArrayMultiaryBase

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
class MPSNDArrayMultiaryBase
```

```objc
@interface MPSNDArrayMultiaryBase : MPSKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](./mpsndarraymultiarybase/init%28coder,device%29.md)
- [init(device: any MTLDevice, sourceCount: Int)](./mpsndarraymultiarybase/init%28device,sourcecount%29.md)
### Instance Properties
- [var destinationArrayAllocator: any MPSNDArrayAllocator](./mpsndarraymultiarybase/destinationarrayallocator.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsndarraymultiarybase/copy%28with,device%29.md)
- [func destinationArrayDescriptor(forSourceArrays: [MPSNDArray], sourceState: MPSState?) -> MPSNDArrayDescriptor](./mpsndarraymultiarybase/destinationarraydescriptor%28forsourcearrays,sourcestate%29.md)
- [func dilationRates(forSourceIndex: Int) -> MPSNDArraySizes](./mpsndarraymultiarybase/dilationrates%28forsourceindex%29.md)
- [func edgeMode(atSourceIndex: Int) -> MPSImageEdgeMode](./mpsndarraymultiarybase/edgemode%28atsourceindex%29.md)
- [func encode(with: NSCoder)](./mpsndarraymultiarybase/encode%28with%29.md)
- [func kernelSizes(forSourceIndex: Int) -> MPSNDArraySizes](./mpsndarraymultiarybase/kernelsizes%28forsourceindex%29.md)
- [func offsets(atSourceIndex: Int) -> MPSNDArrayOffsets](./mpsndarraymultiarybase/offsets%28atsourceindex%29.md)
- [func resultState(forSourceArrays: [MPSNDArray], sourceStates: [MPSState]?, destinationArray: MPSNDArray) -> MPSState?](./mpsndarraymultiarybase/resultstate%28forsourcearrays,sourcestates,destinationarray%29.md)
- [func strides(forSourceIndex: Int) -> MPSNDArrayOffsets](./mpsndarraymultiarybase/strides%28forsourceindex%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Inherited By
- [MPSNDArrayMultiaryGradientKernel](./mpsndarraymultiarygradientkernel.md)
- [MPSNDArrayMultiaryKernel](./mpsndarraymultiarykernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarybase)*