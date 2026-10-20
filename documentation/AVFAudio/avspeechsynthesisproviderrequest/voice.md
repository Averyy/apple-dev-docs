# voice

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The voice to use in the speech request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var voice: AVSpeechSynthesisProviderVoice { get }
```

```objc
@property (nonatomic, readonly) AVSpeechSynthesisProviderVoice * voice;
```

## See Also

### Inspecting a request
- [var ssmlRepresentation: String](./ssmlrepresentation.md)
  The description of the text to synthesize.
- [class AVSpeechSynthesisProviderVoice](../avspeechsynthesisprovidervoice.md)
  An object that represents a voice that an audio unit provides to its host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisproviderrequest/voice)*