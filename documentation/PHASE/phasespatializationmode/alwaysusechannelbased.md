# PHASESpatializationMode.alwaysUseChannelBased

**Framework**: PHASE  
**Kind**: case

A mode that adds a 3D position and orientation to sound by panning across the available output channels.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case alwaysUseChannelBased
```

#### Discussion

The framework selects a channel layout for the output audio that’s compatible with the device’s channel configuration in Settings.

This mode applies the same effect regardless of the current output device.

## See Also

- [PHASESpatializationMode.automatic](phasespatializationmode/automatic.md)
  A mode that indicates that the framework chooses the spatialization mode.
- [PHASESpatializationMode.alwaysUseBinaural](phasespatializationmode/alwaysusebinaural.md)
  A mode that introduces special processing to replicate a realistic spatial listening experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatializationmode/alwaysusechannelbased)*