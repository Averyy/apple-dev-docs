# MPSNNPad

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.0+
- macOS 10.14.1+
- tvOS 12.1+
- visionOS 1.0+

## Declaration

```swift
class MPSNNPad
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnnpad/init(coder:device:).md)
- [convenience init(device: any MTLDevice)](mpsnnpad/init(device:).md)
- [convenience init(device: any MTLDevice, paddingSizeBefore: MPSImageCoordinate, paddingSizeAfter: MPSImageCoordinate)](mpsnnpad/init(device:paddingsizebefore:paddingsizeafter:).md)
- [init(device: any MTLDevice, paddingSizeBefore: MPSImageCoordinate, paddingSizeAfter: MPSImageCoordinate, fillValueArray: Data?)](mpsnnpad/init(device:paddingsizebefore:paddingsizeafter:fillvaluearray:).md)
### Instance Properties
- [var fillValue: Float](mpsnnpad/fillvalue.md)
- [var paddingSizeAfter: MPSImageCoordinate](mpsnnpad/paddingsizeafter.md)
- [var paddingSizeBefore: MPSImageCoordinate](mpsnnpad/paddingsizebefore.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpad)*