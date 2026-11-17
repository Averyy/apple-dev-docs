# CPPlaybackConfiguration.Action

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The action to perform when someone selects the item.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
enum Action
```

```c
enum CPPlaybackAction : NSInteger;
```

## Overview

These constants specify the automatic actions the system can take when someone selects media items in a list. These actions offer a convenient way to start, stop, or restart playback of an item when someone selects it in your app’s interface. If you prefer to handle these actions yourself, choose the [`CPPlaybackConfiguration.Action.none`](./action/none.md) option and use your app’s code to manage playback.

## Topics

### Enumeration Cases
- [CPPlaybackConfiguration.Action.none](./action/none.md)
  An option to do nothing when someone selects the item.
- [CPPlaybackConfiguration.Action.pause](./action/pause.md)
  An option to pause playback.
- [CPPlaybackConfiguration.Action.play](./action/play.md)
  An option to start or resume playback.
- [CPPlaybackConfiguration.Action.replay](./action/replay.md)
  An option to start playback of the item from the beginning.
### Initializers
- [init?(rawValue: Int)](./action/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/action)*