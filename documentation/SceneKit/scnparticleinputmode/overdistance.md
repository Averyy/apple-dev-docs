# SCNParticleInputMode.overDistance

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

The controller’s effect on a particle property is a function of the particle’s distance from the position of a specified node.

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
case overDistance
```

```c
SCNParticleInputModeOverDistance
```

#### Discussion

Use the [`inputOrigin`](../scnparticlepropertycontroller/inputorigin.md) property to specify the node to measure distance from, and the [`inputBias`](../scnparticlepropertycontroller/inputbias.md) and [`inputScale`](../scnparticlepropertycontroller/inputscale.md) properties to refine the relationship between a range of distances into a range of input values for the controller’s animation.

## See Also

### Constants
- [SCNParticleInputMode.overLife](./overlife.md)
  The controller’s effect on a particle property is a function of the time since the particle’s birth.
- [SCNParticleInputMode.overOtherProperty](./overotherproperty.md)
  The controller’s effect on a particle property is a function of another of the particle’s properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleinputmode/overdistance)*