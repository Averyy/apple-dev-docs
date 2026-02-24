# PHASESpatializationMode.automatic

**Framework**: PHASE  
**Kind**: case

A mode that indicates that the framework chooses the spatialization mode.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case automatic
```

#### Discussion

This setting instructs the framework to automatically set a mode that determines how PHASE positions and orients sound in 3D space. The framework chooses a mode based on the output device:

- **`PHASESpatializationMode.binaural`**: Headphones (Bluetooth or line output) and the internal speakers of supported Mac or iOS devices.
- **`PHASESpatializationMode.channelBased`**: External speakers with 2 or more channels.

## See Also

- [PHASESpatializationMode.alwaysUseBinaural](phasespatializationmode/alwaysusebinaural.md)
  A mode that introduces special processing to replicate a realistic spatial listening experience.
- [PHASESpatializationMode.alwaysUseChannelBased](phasespatializationmode/alwaysusechannelbased.md)
  A mode that adds a 3D position and orientation to sound by panning across the available output channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatializationmode/automatic)*