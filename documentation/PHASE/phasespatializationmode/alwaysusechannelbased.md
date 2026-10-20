# PHASESpatializationMode.alwaysUseChannelBased

**Framework**: PHASE  
**Kind**: case  
**Role**: Case

A mode that adds a 3D position and orientation to sound by panning across the available output channels.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case alwaysUseChannelBased
```

```c
PHASESpatializationModeAlwaysUseChannelBased
```

#### Discussion

The framework selects a channel layout for the output audio that’s compatible with the device’s channel configuration in Settings.

This mode applies the same effect regardless of the current output device.

## See Also

### Modes
- [PHASESpatializationMode.automatic](./automatic.md)
  A mode that indicates that the framework chooses the spatialization mode.
- [PHASESpatializationMode.alwaysUseBinaural](./alwaysusebinaural.md)
  A mode that introduces special processing to replicate a realistic spatial listening experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatializationmode/alwaysusechannelbased)*