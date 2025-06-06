# distanceModelParameters

**Framework**: PHASE  
**Kind**: property

An effect that changes sound as it carries over a distance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var distanceModelParameters: PHASEDistanceModelParameters? { get set }
```

#### Discussion

Similar to a Doppler effect, this property changes how an audio source sounds as its distance between the listener increases or decreases in 3D space. The available options are:

##### Programmatically Check Sound Dissipation

After setting a value for this property, you can move a looping sound source to tweak the effect to your app’s particular requirements. The following code programmaticaly moves a looping source away from the listener along the z-axis:


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialmixerdefinition/distancemodelparameters)*