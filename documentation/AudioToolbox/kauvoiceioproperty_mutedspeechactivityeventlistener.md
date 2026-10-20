# kAUVoiceIOProperty_MutedSpeechActivityEventListener

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

A property to register a listener that the system calls when it detects speech while the user has the microphone muted.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var kAUVoiceIOProperty_MutedSpeechActivityEventListener: AudioUnitPropertyID { get }
```

```c
kAUVoiceIOProperty_MutedSpeechActivityEventListener
```

#### Discussion

To use this API, your app must implement mute using the [`kAUVoiceIOProperty_MuteOutput`](./kauvoiceioproperty_muteoutput.md) property.

## See Also

### Observing muted speech
- [typealias AUVoiceIOMutedSpeechActivityEventListener](./auvoiceiomutedspeechactivityeventlistener.md)
  A block that the system calls to indicate speech activity while the user has the microphone muted.
- [enum AUVoiceIOSpeechActivityEvent](./auvoiceiospeechactivityevent.md)
  Constants that indicate the state of muted speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioproperty_mutedspeechactivityeventlistener)*