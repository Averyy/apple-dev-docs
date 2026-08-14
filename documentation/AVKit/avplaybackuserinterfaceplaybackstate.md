# AVPlaybackUserInterfacePlaybackState

**Framework**: AVKit  
**Kind**: enum

Describes possible transport states of the playback source.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum AVPlaybackUserInterfacePlaybackState
```

## Topics

### Enumeration Cases
- [AVPlaybackUserInterfacePlaybackState.normal](avplaybackuserinterfaceplaybackstate/normal.md)
  Indicates the source is in a normal state.
- [AVPlaybackUserInterfacePlaybackState.scanning](avplaybackuserinterfaceplaybackstate/scanning.md)
  Indicates the source is scanning forward or backward at an accelerated rate.
- [AVPlaybackUserInterfacePlaybackState.scrubbing](avplaybackuserinterfaceplaybackstate/scrubbing.md)
  Indicates the source is being scrubbed by user interaction with the timeline.
### Initializers
- [init?(rawValue: Int)](avplaybackuserinterfaceplaybackstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol AVPlaybackUserInterfacePlaybackControllable](avplaybackuserinterfaceplaybackcontrollable-9he54.md)
  Provides playback control and state management for media content.
- [struct AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities.md)
  Describes navigation capabilities of the media source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackstate)*