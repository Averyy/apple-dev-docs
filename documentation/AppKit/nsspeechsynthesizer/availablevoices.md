# availableVoices

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Provides the identifiers of the voices available on the system.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
class var availableVoices: [NSSpeechSynthesizer.VoiceName] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * availableVoices;
```

## Return Value

Array of strings representing the identifiers of each voice available on the system.

## See Also

### Related Documentation
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](./setvoice%28_%29.md)
  Sets the receiver’s current voice.
### Getting Speech Synthesizer Information
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](./attributes%28forvoice%29.md)
  Provides the attribute dictionary of a voice.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](./defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceName](./voicename.md)
- [NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](./attributes%28forvoice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/availablevoices)*