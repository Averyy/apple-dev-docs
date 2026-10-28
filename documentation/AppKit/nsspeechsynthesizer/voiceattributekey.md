# NSSpeechSynthesizer.VoiceAttributeKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](./attributes%28forvoice%29.md).

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
struct VoiceAttributeKey
```

```c
typedef NSString * NSVoiceAttributeKey;
```

## Overview

The following are the identifiers of the macOS system voices (defined in `/System/Library/Speech/Voices`):

```objc
com.apple.speech.synthesis.voice.Agnes
com.apple.speech.synthesis.voice.Albert
com.apple.speech.synthesis.voice.Alex
com.apple.speech.synthesis.voice.BadNews
com.apple.speech.synthesis.voice.Bahh
com.apple.speech.synthesis.voice.Bells
com.apple.speech.synthesis.voice.Boing
com.apple.speech.synthesis.voice.Bruce
com.apple.speech.synthesis.voice.Bubbles
com.apple.speech.synthesis.voice.Cellos
com.apple.speech.synthesis.voice.Deranged
com.apple.speech.synthesis.voice.Fred
com.apple.speech.synthesis.voice.GoodNews
com.apple.speech.synthesis.voice.Hysterical
com.apple.speech.synthesis.voice.Junior
com.apple.speech.synthesis.voice.Kathy
com.apple.speech.synthesis.voice.Organ
com.apple.speech.synthesis.voice.Princess
com.apple.speech.synthesis.voice.Ralph
com.apple.speech.synthesis.voice.Trinoids
com.apple.speech.synthesis.voice.Vicki
com.apple.speech.synthesis.voice.Victoria
com.apple.speech.synthesis.voice.Whisper
com.apple.speech.synthesis.voice.Zarvox
```

## Topics

### Voice Attribute Keys
- [static let identifier: NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey/identifier.md)
  A unique string identifying the voice. The identifiers of the system voices are listed in `Listing 1`.
- [static let name: NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey/name.md)
  The name of the voice suitable for display. An `NSString`.
- [static let age: NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey/age.md)
  The perceived age (in years) of the voice. An `NSString`
- [static let gender: NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey/gender.md)
  The perceived gender of the voice. The supported values are listed in `Voice Gender Keys`.  An `NSString`
- [static let demoText: NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey/demotext.md)
  A demonstration string to speak. An `NSString`
- [static let localeIdentifier: NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey/localeidentifier.md)
  The language of the voice.  An `NSString`
- [static let supportedCharacters: NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey/supportedcharacters.md)
  A list of Unicode character id ranges that define the Unicode characters supported by this voice.
- [static let individuallySpokenCharacters: NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey/individuallyspokencharacters.md)
  A list of Unicode character id ranges that define the Unicode characters that can be spoken in character-by-character mode by this voice.
### Initializers
- [init(rawValue: String)](./voiceattributekey/init%28rawvalue%29.md)
### Deprecated
- [NSVoiceLanguage](../nsvoicelanguage.md)
  The language of the voice (currently US English only). An `NSString`

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Speech Synthesizer Information
- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](./availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](./attributes%28forvoice%29.md)
  Provides the attribute dictionary of a voice.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](./defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceName](./voicename.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/voiceattributekey)*