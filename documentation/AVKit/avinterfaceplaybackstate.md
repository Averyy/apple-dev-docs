# AVInterfacePlaybackState

**Framework**: AVKit  
**Kind**: enum

Describes possible playback states of the interface source.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum AVInterfacePlaybackState
```

## Topics

### Creating a playback state
- [init?(rawValue: Int)](avinterfaceplaybackstate/init(rawvalue:).md)
### Playback States
- [AVInterfacePlaybackState.normal](avinterfaceplaybackstate/normal.md)
  Indicates the source is in a normal state.
- [AVInterfacePlaybackState.scanning](avinterfaceplaybackstate/scanning.md)
  Indicates the source is scanning forward or backward at an accelerated rate.
- [AVInterfacePlaybackState.scrubbing](avinterfaceplaybackstate/scrubbing.md)
  Indicates the source is being scrubbed by user interaction with the timeline.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AVInterfacePlaybackControllable](avinterfaceplaybackcontrollable-44aba.md)
  Provides playback control and state management for media content.
- [struct AVInterfaceSeekCapabilities](avinterfaceseekcapabilities.md)
  Describes navigation capabilities of the media source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfaceplaybackstate)*