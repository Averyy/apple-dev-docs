# setMutedSpeechActivityEventListener(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setMutedSpeechActivityEventListener(_ listenerBlock: (@Sendable (AVAudioVoiceProcessingSpeechActivityEvent) -> Void)?) -> Bool
```

```objc
- (BOOL) setMutedSpeechActivityEventListener:(void (^)(AVAudioVoiceProcessingSpeechActivityEvent event)) listenerBlock;
```

## See Also

### Handling muted speech events
- [enum AVAudioVoiceProcessingSpeechActivityEvent](../avaudiovoiceprocessingspeechactivityevent.md)
  Types of speech activity events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioinputnode/setmutedspeechactivityeventlistener(_:))*