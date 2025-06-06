# AUVoiceIOMutedSpeechActivityEventListener

**Framework**: Audio Toolbox  
**Kind**: typealias

A block that the system calls to indicate speech activity while the user has the microphone muted.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUVoiceIOMutedSpeechActivityEventListener = (AUVoiceIOSpeechActivityEvent) -> Void
```

## Parameters

- `event`: An event that indicates whether muted speech started or ended.

## See Also

- [var kAUVoiceIOProperty_MutedSpeechActivityEventListener: AudioUnitPropertyID](kauvoiceioproperty_mutedspeechactivityeventlistener.md)
  A property to register a listener that the system calls when it detects speech while the user has the microphone muted.
- [enum AUVoiceIOSpeechActivityEvent](auvoiceiospeechactivityevent.md)
  Constants that indicate the state of muted speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auvoiceiomutedspeechactivityeventlistener)*