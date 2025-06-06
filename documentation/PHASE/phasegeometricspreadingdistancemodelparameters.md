# PHASEGeometricSpreadingDistanceModelParameters

**Framework**: PHASE  
**Kind**: class

An object that dissipates sound frequencies over distance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEGeometricSpreadingDistanceModelParameters
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Overview

This class implements a  effect — a strategy that aims to model the real-world manner in which sound changes with distance. When the distance between a sound and listener changes, the roll-off effect dissipates certain audio frequencies more than others.

##### Dissipate Sound By Choosing a Roll Off Factor

PHASE emphasizes or deemphasizes the volume loss of the mixer’s sound sources based on the [`rolloffFactor`](phasegeometricspreadingdistancemodelparameters/rollofffactor.md) you choose. For example, a [`rolloffFactor`](phasegeometricspreadingdistancemodelparameters/rollofffactor.md) of `1.0` reduces sound between the source and listener by 6 dB for every doubling of distance. At `2.0`, the loss doubles. At `0.5`, the loss halves.

To add a geometric-spreading distance model to a spatial sounds, set the mixer’s [`distanceModelParameters`](phasespatialmixerdefinition/distancemodelparameters.md) property to an instance of this class. For example:

## Topics

### Creating the Distance Model Parameters
- [init()](phasegeometricspreadingdistancemodelparameters/init.md)
  Creates the geometric spreading distance model parameters.
### Setting the Roll-Off Factor
- [var rolloffFactor: Double](phasegeometricspreadingdistancemodelparameters/rollofffactor.md)
  A value that fades specific frequencies over a distance.

## Relationships

### Inherits From
- [PHASEDistanceModelParameters](phasedistancemodelparameters.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEEnvelopeDistanceModelParameters](phaseenvelopedistancemodelparameters.md)
  A graph of points and curves that shapes the volume of a sound over distance.
- [class PHASEDistanceModelFadeOutParameters](phasedistancemodelfadeoutparameters.md)
  A distance over which the framework fades out sound.
- [class PHASEDistanceModelParameters](phasedistancemodelparameters.md)
  A base class for a sound’s rate of change over distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegeometricspreadingdistancemodelparameters)*