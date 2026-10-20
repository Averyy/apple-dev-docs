# init(voice:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes the receiver with a voice.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
init?(voice: NSSpeechSynthesizer.VoiceName?)
```

```objc
- (instancetype) initWithVoice:(NSSpeechSynthesizerVoiceName) voice;
```

#### Return Value

Initialized speech synthesizer or `nil` when the voice identified by `voiceIdentifier` is not available or when there’s an allocation error.

## Parameters

- `voice`: Identifier of the voice to set as the current voice. When `nil`, the default voice is used. Passing in a specific voice means the initial speaking rate is determined by the synthesizer’s default speaking rate; passing `nil` means the speaking rate is automatically set to the rate the user specifies in Speech preferences.

## See Also

### Related Documentation
- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](./availablevoices.md)
  Provides the identifiers of the voices available on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/init(voice:))*