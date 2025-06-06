# PHASECardioidDirectivityModelParameters

**Framework**: PHASE  
**Kind**: class

An object that directs sound in a heart-shaped curve surrounding a sound source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASECardioidDirectivityModelParameters
```

#### Overview

This class configures a particular frequency range in the audio spectrum that emits sound in an area defined by a mathematical cardioid. PHASE refers to each frequency segment along the audio spectrum as a . This class contains an array of `subbands` that each can direct sound in a unique cardioid shape. The framework outputs a blend of a frequency’s adjacent subbands for all frequencies that lie outside of those specified in the `subbands` array.

##### Emit Sound in the Shape of a Cardioid

The following code defines a two-band cardioid model. The first subband resembles a heart-shaped cardioid and the second resembles a hypercardioid.

![Illustration of two different types of cardioids that position in relation to a sphere representing the user. On the left, a cardioid resembles a heart with a sphere resting in the heart’s cusp. On the right, a cardioid resembles the shape of a hypercardioid. A large oval extends outward from one side of the sphere, and a smaller oval extends in the opposite direction, from the backside of the sphere.](https://docs-assets.developer.apple.com/published/e32a57ccb081e69f684ce2915ce3ce21/media-3919256%402x.png)

## Topics

### Creating the Cardioid Directivity Model Parameters
- [init(subbandParameters: [PHASECardioidDirectivityModelSubbandParameters])](phasecardioiddirectivitymodelparameters/init(subbandparameters:).md)
  Creates an object that directs sound in a heart-shaped curve surrounding a sound source.
### Defining Subbands
- [var subbandParameters: [PHASECardioidDirectivityModelSubbandParameters]](phasecardioiddirectivitymodelparameters/subbandparameters.md)
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

- [class PHASECardioidDirectivityModelSubbandParameters](phasecardioiddirectivitymodelsubbandparameters.md)
  A data set that projects sound of a certain frequency outward in the shape of a heart.
- [class PHASEConeDirectivityModelParameters](phaseconedirectivitymodelparameters.md)
  An object that directs sound in a cone-shaped curve that extends from a sound source.
- [class PHASEConeDirectivityModelSubbandParameters](phaseconedirectivitymodelsubbandparameters.md)
  A data set that projects sound of a certain frequency outward in the shape of a cone.
- [class PHASEDirectivityModelParameters](phasedirectivitymodelparameters.md)
  A base class for objects that direct sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecardioiddirectivitymodelparameters)*