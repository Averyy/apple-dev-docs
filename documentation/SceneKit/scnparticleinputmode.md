# SCNParticleInputMode

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Options for the input value of the property controller’s animation, used by the [`inputMode`](./scnparticlepropertycontroller/inputmode.md) property.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
enum SCNParticleInputMode
```

```c
enum SCNParticleInputMode : NSInteger;
```

## Topics

### Constants
- [SCNParticleInputMode.overLife](./scnparticleinputmode/overlife.md)
  The controller’s effect on a particle property is a function of the time since the particle’s birth.
- [SCNParticleInputMode.overDistance](./scnparticleinputmode/overdistance.md)
  The controller’s effect on a particle property is a function of the particle’s distance from the position of a specified node.
- [SCNParticleInputMode.overOtherProperty](./scnparticleinputmode/overotherproperty.md)
  The controller’s effect on a particle property is a function of another of the particle’s properties.
### Initializers
- [init?(rawValue: Int)](./scnparticleinputmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleinputmode)*