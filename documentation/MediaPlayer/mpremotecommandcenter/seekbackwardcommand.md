# seekBackwardCommand

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The command object for seeking backward through a single media item.

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
var seekBackwardCommand: MPRemoteCommand { get }
```

```objc
@property (nonatomic, readonly) MPRemoteCommand * seekBackwardCommand;
```

## Discussion

Use the object in this property to register your app’s handler for seeking backward in the current track. In your handler, begin seeking backward through the current media item. You can disable the command if your app does not support it.

## See Also

### Navigating a track’s contents
- [var changePlaybackRateCommand: MPChangePlaybackRateCommand](./changeplaybackratecommand.md)
  The command object for changing the playback rate of the current media item.
- [var seekForwardCommand: MPRemoteCommand](./seekforwardcommand.md)
  The command object for seeking forward through a single media item.
- [var skipBackwardCommand: MPSkipIntervalCommand](./skipbackwardcommand.md)
  The command object for playing a previous point in a media item.
- [var skipForwardCommand: MPSkipIntervalCommand](./skipforwardcommand.md)
  The command object for playing a future point in a media item.
- [var changePlaybackPositionCommand: MPChangePlaybackPositionCommand](./changeplaybackpositioncommand.md)
  The command object for changing the playback position in a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/seekbackwardcommand)*