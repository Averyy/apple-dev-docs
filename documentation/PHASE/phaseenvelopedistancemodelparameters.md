# PHASEEnvelopeDistanceModelParameters

**Framework**: PHASE  
**Kind**: class

A graph of points and curves that shapes the volume of a sound over distance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEEnvelopeDistanceModelParameters
```

#### Overview

This class provides an envelope that the app configures to dissipate the volume of a source’s sound with distance. The envelope describes a graph that the app configures using points and curves, where the input value is the distance between a sound source and the listener, and the output value is the sound’s volume.

##### Dissipate Sound By Using an Envelope

The framework interprets this class’s envelope as a , which determines the sound’s volume over a distance. An envelope offers more precise control over sound dissipation than a geometric [`rolloffFactor`](phasegeometricspreadingdistancemodelparameters/rollofffactor.md). For example, the following code defines slow sound dissipation followed by a sharp decrease:

## Topics

### Creating the Distance Model Parameters
- [init(envelope: PHASEEnvelope)](phaseenvelopedistancemodelparameters/init(envelope:).md)
  Creates the distance model parameters with an envelope.
### Shaping the Volume Over a Distance
- [var envelope: PHASEEnvelope](phaseenvelopedistancemodelparameters/envelope.md)
  An envelope that shapes sound dissipation over distance.

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

- [class PHASEGeometricSpreadingDistanceModelParameters](phasegeometricspreadingdistancemodelparameters.md)
  An object that dissipates sound frequencies over distance.
- [class PHASEDistanceModelFadeOutParameters](phasedistancemodelfadeoutparameters.md)
  A distance over which the framework fades out sound.
- [class PHASEDistanceModelParameters](phasedistancemodelparameters.md)
  A base class for a sound’s rate of change over distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelopedistancemodelparameters)*