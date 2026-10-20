# MPSTemporalAA

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
class MPSTemporalAA
```

```objc
@interface MPSTemporalAA : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpstemporalaa/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpstemporalaa/init%28device%29.md)
### Instance Properties
- [var blendFactor: Float](./mpstemporalaa/blendfactor.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpstemporalaa/copy%28with,device%29.md)
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthTexture: (any MTLTexture)?)](./mpstemporalaa/encode%28to,sourcetexture,previoustexture,destinationtexture,motionvectortexture,depthtexture%29.md)
- [func encode(with: NSCoder)](./mpstemporalaa/encode%28with%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporalaa)*