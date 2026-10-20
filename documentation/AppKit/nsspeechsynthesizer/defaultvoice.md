# defaultVoice

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Provides the identifier of the default voice.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
class var defaultVoice: NSSpeechSynthesizer.VoiceName { get }
```

```objc
@property (class, copy, readonly) NSSpeechSynthesizerVoiceName defaultVoice;
```

#### Return Value

Identifier of the default voice.

## See Also

### Getting Speech Synthesizer Information
- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](./availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](./attributes%28forvoice%29.md)
  Provides the attribute dictionary of a voice.
- [NSSpeechSynthesizer.VoiceName](./voicename.md)
- [NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](./attributes%28forvoice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/defaultvoice)*