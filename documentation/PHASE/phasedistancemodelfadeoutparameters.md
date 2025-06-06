# PHASEDistanceModelFadeOutParameters

**Framework**: PHASE  
**Kind**: class

A distance over which the framework fades out sound.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEDistanceModelFadeOutParameters
```

#### Overview

For spatial sound output, the framework stops playing a sound when its distance from the listener surpases [`cullDistance`](phasedistancemodelfadeoutparameters/culldistance.md). The framework gradually fades out the sound’s volume as the distance between the source and listener approaches [`cullDistance`](phasedistancemodelfadeoutparameters/culldistance.md). Likewise, the framework gradually fades in the sound as the distance between the source and listener approaches `0`. A [`PHASEDistanceModelParameters`](phasedistancemodelparameters.md) object provides an instance of this class to a spatial mixer; for more information, see [`fadeOutParameters`](phasedistancemodelparameters/fadeoutparameters.md).

##### Specifying a Maximum Distance That Sound Reaches

The following code demonstrates a spatial mixer’s additional fade out. By setting `fadeOutLength` to `1.0`, the framework begins to fade out a sound after its distance to the listener surpases `1.0`.

## Topics

### Creating the Distance Model Fade-Out Parameters
- [init(cullDistance: Double)](phasedistancemodelfadeoutparameters/init(culldistance:).md)
  Creates a distance beyond which sound sources stop playing.
### Inspecting the Cull Distance
- [var cullDistance: Double](phasedistancemodelfadeoutparameters/culldistance.md)
  The distance beyond which the framework doesn’t process the sound.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class PHASEEnvelopeDistanceModelParameters](phaseenvelopedistancemodelparameters.md)
  A graph of points and curves that shapes the volume of a sound over distance.
- [class PHASEDistanceModelParameters](phasedistancemodelparameters.md)
  A base class for a sound’s rate of change over distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasedistancemodelfadeoutparameters)*