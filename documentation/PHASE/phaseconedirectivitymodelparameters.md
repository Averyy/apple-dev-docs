# PHASEConeDirectivityModelParameters

**Framework**: PHASE  
**Kind**: class

An object that directs sound in a cone-shaped curve that extends from a sound source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEConeDirectivityModelParameters
```

#### Overview

This class determines that a particular frequency range in the audio spectrum emits sound in an area defined by a mathematical cone. PHASE refers to each frequency segment along the audio spectrum as a . This class contains an array of `subbands` that each direct sound in a unique cone shape. The framework outputs a blend of a frequency’s adjacent subbands for all frequencies that lie outside of those specified in the `subbands` array.

##### Emit Sound in the Shape of a Cone

The following code defines a cone directivity model with two subbands. The first subband emits sound in a narrow region and the second subband outputs sound in a wider region.

![An illustration of two different cone directivity configurations. On the left, a narrow cone contains a slightly narrower cone. A callout extends from the outer cone’s point that indicates its angle is 40 degrees. A callout extends from the inner cone’s point that indicates its angle is 30 degrees. On the right, a wide cone rests inside a slightly wider cone. A callout extends from the outer cone’s point that indicates its angle is 80 degrees. A callout extends from the inner cone’s point that indicates its angle is 60 degrees. In both configurations, a sphere rests on the cone’s point to indicate the user’s position in relation to the cone. ](https://docs-assets.developer.apple.com/published/404f1ffecbdcd82570920028c583e831/media-3887365%402x.png)

## Topics

### Creating the Cone Directivity Model Parameters
- [init(subbandParameters: [PHASEConeDirectivityModelSubbandParameters])](phaseconedirectivitymodelparameters/init(subbandparameters:).md)
  Creates an object that directs sound in a cone-shaped curve that extends from a sound source.
### Defining Subbands
- [var subbandParameters: [PHASEConeDirectivityModelSubbandParameters]](phaseconedirectivitymodelparameters/subbandparameters.md)
  An array of frequencies that describe varying sound emission across the spectrum.

## Relationships

### Inherits From
- [PHASEDirectivityModelParameters](phasedirectivitymodelparameters.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASECardioidDirectivityModelParameters](phasecardioiddirectivitymodelparameters.md)
  An object that directs sound in a heart-shaped curve surrounding a sound source.
- [class PHASECardioidDirectivityModelSubbandParameters](phasecardioiddirectivitymodelsubbandparameters.md)
  A data set that projects sound of a certain frequency outward in the shape of a heart.
- [class PHASEConeDirectivityModelSubbandParameters](phaseconedirectivitymodelsubbandparameters.md)
  A data set that projects sound of a certain frequency outward in the shape of a cone.
- [class PHASEDirectivityModelParameters](phasedirectivitymodelparameters.md)
  A base class for objects that direct sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseconedirectivitymodelparameters)*