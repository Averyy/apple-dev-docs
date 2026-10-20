# AVPlaybackUserInterfacePlaybackState

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

Describes possible transport states of the playback source.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum AVPlaybackUserInterfacePlaybackState
```

```c
enum AVPlaybackUserInterfacePlaybackState : NSInteger;
```

## Topics

### Enumeration Cases
- [AVPlaybackUserInterfacePlaybackState.normal](./avplaybackuserinterfaceplaybackstate/normal.md)
  Indicates the source is in a normal state.
- [AVPlaybackUserInterfacePlaybackState.scanning](./avplaybackuserinterfaceplaybackstate/scanning.md)
  Indicates the source is scanning forward or backward at an accelerated rate.
- [AVPlaybackUserInterfacePlaybackState.scrubbing](./avplaybackuserinterfaceplaybackstate/scrubbing.md)
  Indicates the source is being scrubbed by user interaction with the timeline.
### Initializers
- [init?(rawValue: Int)](./avplaybackuserinterfaceplaybackstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Playback control
- [protocol AVPlaybackUserInterfacePlaybackControllable](./avplaybackuserinterfaceplaybackcontrollable-9he54.md)
  Provides playback control and state management for media content.
- [struct AVPlaybackUserInterfaceSeekCapabilities](./avplaybackuserinterfaceseekcapabilities.md)
  Describes navigation capabilities of the media source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackstate)*