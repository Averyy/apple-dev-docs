# AudioFileResource.Configuration

**Framework**: RealityKit  
**Kind**: struct

A container for various settings for loading an audio file resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(loadingStrategy:shouldLoop:shouldRandomizeStartTime:normalization:calibration:mixGroupName:)](audiofileresource/configuration-9pm1g/init(loadingstrategy:shouldloop:shouldrandomizestarttime:normalization:calibration:mixgroupname:).md)
  Initializes a new audio file resource configuration.
### Instance Properties
- [var calibration: AudioResource.Calibration?](audiofileresource/configuration-461s2/calibration.md)
  Stores the calibration setting that the system applies to the audio resource, ensuring optimal playback quality.
- [var loadingStrategy: AudioFileResource.LoadingStrategy](audiofileresource/configuration-461s2/loadingstrategy.md)
  Stores the strategy the system uses for handling an audio resource’s data before and during playback.
- [var mixGroupName: String?](audiofileresource/configuration-461s2/mixgroupname.md)
  An arbitrary name that can assigns an audio resource to an audio mix group.
- [var normalization: AudioResource.Normalization?](audiofileresource/configuration-461s2/normalization.md)
  Stores the normalization portion of the configuration.
- [var shouldLoop: Bool](audiofileresource/configuration-461s2/shouldloop.md)
  Stores a Boolean indicating whether the playback loops infinitely, until manually stopped or paused.
- [var shouldRandomizeStartTime: Bool](audiofileresource/configuration-461s2/shouldrandomizestarttime.md)
  Stores a Boolean indicating whether the playback begins from the start of the file, or from a random position.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/configuration-461s2)*