# speechVoices

**Framework**: AVFAudio  
**Kind**: property

A list of voices the audio unit provides to the system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var speechVoices: [AVSpeechSynthesisProviderVoice] { get set }
```

#### Discussion

The list of voices that a user selects through Settings. Speech synthesizer audio unit extensions must provide this list. Override the getter to perform complex fetches that provide a dynamic list of voices.

## See Also

- [class AVSpeechSynthesisProviderVoice](avspeechsynthesisprovidervoice.md)
  An object that represents a voice that an audio unit provides to its host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovideraudiounit/speechvoices)*