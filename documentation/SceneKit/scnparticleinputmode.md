# SCNParticleInputMode

**Framework**: SceneKit  
**Kind**: enum

Options for the input value of the property controller’s animation, used by the [`inputMode`](scnparticlepropertycontroller/inputmode.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum SCNParticleInputMode
```

## Topics

### Constants
- [SCNParticleInputMode.overLife](scnparticleinputmode/overlife.md)
  The controller’s effect on a particle property is a function of the time since the particle’s birth.
- [SCNParticleInputMode.overDistance](scnparticleinputmode/overdistance.md)
  The controller’s effect on a particle property is a function of the particle’s distance from the position of a specified node.
- [SCNParticleInputMode.overOtherProperty](scnparticleinputmode/overotherproperty.md)
  The controller’s effect on a particle property is a function of another of the particle’s properties.
### Initializers
- [init?(rawValue: Int)](scnparticleinputmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleinputmode)*