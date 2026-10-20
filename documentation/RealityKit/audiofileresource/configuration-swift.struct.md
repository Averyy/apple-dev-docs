# AudioFileResource.Configuration

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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
- [init(loadingStrategy: AudioFileResource.LoadingStrategy, shouldLoop: Bool, shouldRandomizeStartTime: Bool, normalization: AudioResource.Normalization?, calibration: AudioResource.Calibration?, mixGroupName: String?)](./configuration-swift.struct/init%28loadingstrategy,shouldloop,shouldrandomizestarttime,normalization,calibration,mixgroupname%29.md)
  Initializes a new audio file resource configuration.
### Configuring the loading optimization strategy
- [var loadingStrategy: AudioFileResource.LoadingStrategy](./configuration-swift.struct/loadingstrategy.md)
  Stores the strategy the system uses for handling an audio resource’s data before and during playback.
### Controlling the volume
- [var normalization: AudioResource.Normalization?](./configuration-swift.struct/normalization.md)
  Stores the normalization portion of the configuration.
- [var calibration: AudioResource.Calibration?](./configuration-swift.struct/calibration.md)
  Stores the calibration setting that the system applies to the audio resource, ensuring optimal playback quality.
### Customizing the playback
- [var shouldRandomizeStartTime: Bool](./configuration-swift.struct/shouldrandomizestarttime.md)
  Stores a Boolean indicating whether the playback begins from the start of the file, or from a random position.
- [var shouldLoop: Bool](./configuration-swift.struct/shouldloop.md)
  Stores a Boolean indicating whether the playback loops infinitely, until manually stopped or paused.
### Assigning an audio resource to a mix group
- [var mixGroupName: String?](./configuration-swift.struct/mixgroupname.md)
  An arbitrary name that can assigns an audio resource to an audio mix group.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [AudioFileResource.LoadingStrategy](./loadingstrategy-swift.enum.md)
  A container for different strategies on how to handle resources’ data before and during playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/configuration-swift.struct)*