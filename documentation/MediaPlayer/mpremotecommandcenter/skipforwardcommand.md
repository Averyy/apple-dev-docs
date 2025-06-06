# skipForwardCommand

**Framework**: Media Player  
**Kind**: property

The command object for playing a future point in a media item.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var skipForwardCommand: MPSkipIntervalCommand { get }
```

#### Discussion

Use the object in this property to register your app’s handler for jumping to a future point in the current track. In your handler, skip forward by the amount specified in the event’s [`interval`](mpskipintervalcommandevent/interval.md) property. You can disable the command if your app does not support it.

## See Also

- [var changePlaybackRateCommand: MPChangePlaybackRateCommand](mpremotecommandcenter/changeplaybackratecommand.md)
  The command object for changing the playback rate of the current media item.
- [var seekBackwardCommand: MPRemoteCommand](mpremotecommandcenter/seekbackwardcommand.md)
  The command object for seeking backward through a single media item.
- [var seekForwardCommand: MPRemoteCommand](mpremotecommandcenter/seekforwardcommand.md)
  The command object for seeking forward through a single media item.
- [var skipBackwardCommand: MPSkipIntervalCommand](mpremotecommandcenter/skipbackwardcommand.md)
  The command object for playing a previous point in a media item.
- [var changePlaybackPositionCommand: MPChangePlaybackPositionCommand](mpremotecommandcenter/changeplaybackpositioncommand.md)
  The command object for changing the playback position in a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/skipforwardcommand)*