# MPSNNPad

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSNNPad : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsnnpad/init%28coder,device%29.md)
- [convenience init(device: any MTLDevice)](./mpsnnpad/init%28device%29.md)
- [convenience init(device: any MTLDevice, paddingSizeBefore: MPSImageCoordinate, paddingSizeAfter: MPSImageCoordinate)](./mpsnnpad/init%28device,paddingsizebefore,paddingsizeafter%29.md)
- [init(device: any MTLDevice, paddingSizeBefore: MPSImageCoordinate, paddingSizeAfter: MPSImageCoordinate, fillValueArray: Data?)](./mpsnnpad/init%28device,paddingsizebefore,paddingsizeafter,fillvaluearray%29.md)
### Instance Properties
- [var fillValue: Float](./mpsnnpad/fillvalue.md)
- [var paddingSizeAfter: MPSImageCoordinate](./mpsnnpad/paddingsizeafter.md)
- [var paddingSizeBefore: MPSImageCoordinate](./mpsnnpad/paddingsizebefore.md)

## Relationships

### Inherits From
- [MPSCNNKernel](./mpscnnkernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpad)*