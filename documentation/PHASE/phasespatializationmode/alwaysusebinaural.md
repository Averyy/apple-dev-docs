# PHASESpatializationMode.alwaysUseBinaural

**Framework**: PHASE  
**Kind**: case

A mode that introduces special processing to replicate a realistic spatial listening experience.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case alwaysUseBinaural
```

#### Discussion

Enable this mode to override a system or user preference and implement binaural audio output. When binaural mode plays through internal speakers on supported Apple devices, the framework applies additional effects to the output to achieve a sound experience comparable to one with headphones.

## See Also

- [PHASESpatializationMode.automatic](phasespatializationmode/automatic.md)
  A mode that indicates that the framework chooses the spatialization mode.
- [PHASESpatializationMode.alwaysUseChannelBased](phasespatializationmode/alwaysusechannelbased.md)
  A mode that adds a 3D position and orientation to sound by panning across the available output channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatializationmode/alwaysusebinaural)*