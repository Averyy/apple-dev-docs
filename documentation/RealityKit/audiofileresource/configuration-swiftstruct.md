# AudioFileResource.Configuration

**Framework**: RealityKit  
**Kind**: struct

A container for various settings for loading an audio file resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration for an audio file resource
- [init(loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool, shouldRandomizeStartTime: Bool, normalization: AudioResource.Normalization?, calibration: AudioResource.Calibration?, mixGroupName: String?)](audiofileresource/configuration-swift.struct/init(loadingstrategy:shouldloop:shouldrandomizestarttime:normalization:calibration:mixgroupname:).md)
  Initializes a new audio file resource configuration.
### Configuring the loading optimization strategy
- [var loadingStrategy: AudioFileResource.LoadingStrategy](audiofileresource/configuration-swift.struct/loadingstrategy.md)
  Stores the strategy the system uses for handling an audio resource’s data before and during playback.
### Controlling the volume
- [var normalization: AudioResource.Normalization?](audiofileresource/configuration-swift.struct/normalization.md)
  Stores the normalization portion of the configuration.
- [var calibration: AudioResource.Calibration?](audiofileresource/configuration-swift.struct/calibration.md)
  Stores the calibration setting that the system applies to the audio resource, ensuring optimal playback quality.
### Customizing the playback
- [var shouldRandomizeStartTime: Bool](audiofileresource/configuration-swift.struct/shouldrandomizestarttime.md)
  Stores a Boolean indicating whether the playback begins from the start of the file, or from a random position.
- [var shouldLoop: Bool](audiofileresource/configuration-swift.struct/shouldloop.md)
  Stores a Boolean indicating whether the playback loops infinitely, until manually stopped or paused.
### Assigning an audio resource to a mix group
- [var mixGroupName: String?](audiofileresource/configuration-swift.struct/mixgroupname.md)
  An arbitrary name that can assigns an audio resource to an audio mix group.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AudioFileResource.LoadingStrategy](audiofileresource/loadingstrategy-swift.enum.md)
  A container for different strategies on how to handle resources’ data before and during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/configuration-swift.struct)*