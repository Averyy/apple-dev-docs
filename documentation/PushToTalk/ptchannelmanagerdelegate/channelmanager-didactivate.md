# channelManager(_:didActivate:)

**Framework**: Push to Talk  
**Kind**: method  
**Required**: Yes

Tells the observer the audio session activated.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func channelManager(_ channelManager: PTChannelManager, didActivate audioSession: AVAudioSession)
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Discussion

Before recording and transmitting audio, wait for the framework to call this method. The framework calls the method when the audio session is active and set to the correct priority, and allows for recording audio even if the app is in the background. The framework doesn’t call the method if the channel transmission mode is [`PTTransmissionMode.fullDuplex`](pttransmissionmode/fullduplex.md), and already has an active audio session because it’s receiving audio from a remote participant when a transmission begins.

## Parameters

- `channelManager`: The channel manager.
- `audioSession`: The audio session that activated.

## See Also

- [func channelManager(PTChannelManager, didDeactivate: AVAudioSession)](ptchannelmanagerdelegate/channelmanager(_:diddeactivate:).md)
  Tells the observer the audio session deactivated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:didactivate:))*