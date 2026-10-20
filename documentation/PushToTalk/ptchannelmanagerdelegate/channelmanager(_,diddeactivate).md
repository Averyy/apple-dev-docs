# channelManager(_:didDeactivate:)

**Framework**: Push to Talk  
**Kind**: method  
**Required**: Yes

Tells the observer the audio session deactivated.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func channelManager(_ channelManager: PTChannelManager, didDeactivate audioSession: AVAudioSession)
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

## Parameters

- `channelManager`: The channel manager.
- `audioSession`: The audio session that deactivated.

## See Also

- [func channelManager(PTChannelManager, didActivate: AVAudioSession)](ptchannelmanagerdelegate/channelmanager(_:didactivate:).md)
  Tells the observer the audio session activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:diddeactivate:))*