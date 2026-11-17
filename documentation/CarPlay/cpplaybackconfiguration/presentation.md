# CPPlaybackConfiguration.Presentation

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the presentation style for the media of a selected item.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
enum Presentation
```

```c
enum CPPlaybackPresentation : NSInteger;
```

## Overview

These constants specify the presentation style to apply to media items in a list when someone selects them. The system can present system media interfaces automatically in response to interactions. For example, when someone selects an audio item, the system can show your app’s Now Playing interface and configure it to display the item. If you prefer to present your app’s media interface, choose the [`CPPlaybackConfiguration.Presentation.none`](./presentation/none.md) option and configure the interface using your custom code.

## Topics

### Enumeration Cases
- [CPPlaybackConfiguration.Presentation.audio](./presentation/audio.md)
  An option to display the Now Playing interface automatically and configure it with the item.
- [CPPlaybackConfiguration.Presentation.none](./presentation/none.md)
  An option to handle media selections from your app.
- [CPPlaybackConfiguration.Presentation.video](./presentation/video.md)
  An option to display the system video player automatically if it’s available and supported.
### Initializers
- [init?(rawValue: Int)](./presentation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/presentation)*