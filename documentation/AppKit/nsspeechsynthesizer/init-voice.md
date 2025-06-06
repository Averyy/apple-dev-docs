# init(voice:)

**Framework**: AppKit  
**Kind**: init

Initializes the receiver with a voice.

**Availability**:
- macOS 10.3+

## Declaration

```swift
init?(voice: NSSpeechSynthesizer.VoiceName?)
```

#### Return Value

Initialized speech synthesizer or `nil` when the voice identified by `voiceIdentifier` is not available or when there’s an allocation error.

## Parameters

- `voice`: Identifier of the voice to set as the current voice. When  , the default voice is used. Passing in a specific voice means the initial speaking rate is determined by the synthesizer’s default speaking rate; passing   means the speaking rate is automatically set to the rate the user specifies in Speech preferences.

## See Also

- [Speech Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Speech/Speech.html#//apple_ref/doc/uid/10000178i)
- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](nsspeechsynthesizer/availablevoices.md)
  Provides the identifiers of the voices available on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/init(voice:))*