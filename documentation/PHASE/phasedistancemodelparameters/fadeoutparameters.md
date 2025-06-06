# fadeOutParameters

**Framework**: PHASE  
**Kind**: property

A distance over which the framework fades out the mixer’s sound.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var fadeOutParameters: PHASEDistanceModelFadeOutParameters? { get set }
```

#### Discussion

As a sound source’s distance between the listener approaches the value of this property, the framework gradually lowers the sound’s volume to `0`. Beyond this distance, PHASE culls the sound. This property offers an additional fade out that the framework applies on top of the spatial mixer’s [`distanceModelParameters`](phasespatialmixerdefinition/distancemodelparameters.md).

The framework calculates distance as the difference between the listener’s position and the sound-source position, scaled by the engine’s [`unitsPerMeter`](phaseengine/unitspermeter.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasedistancemodelparameters/fadeoutparameters)*