# channelManager(_:didDeactivate:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) channelManager:(PTChannelManager *) channelManager didDeactivateAudioSession:(AVAudioSession *) audioSession;
```

## Mentions

- [Creating a Push to Talk app](../creating-a-push-to-talk-app.md)

## Parameters

- `channelManager`: The channel manager.
- `audioSession`: The audio session that deactivated.

## See Also

### Activating and deactivating the audio session
- [func channelManager(PTChannelManager, didActivate: AVAudioSession)](./channelmanager%28_,didactivate%29.md)
  Tells the observer the audio session activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:diddeactivate:))*