# LocaleDependentSpeechModule

**Framework**: Speech  
**Kind**: protocol

If a module conforms to this protocol, then its assets depend on the locale setting.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol LocaleDependentSpeechModule : SpeechModule
```

## Topics

### Instance Properties
- [var selectedLocales: [Locale]](localedependentspeechmodule/selectedlocales.md)
  A set of locales that are used by the module.
### Type Properties
- [static var supportedLocales: [Locale]](localedependentspeechmodule/supportedlocales.md)
  A set of all possible locales that can be used by the module class.
### Type Methods
- [static func supportedLocale(equivalentTo: Locale) async -> Locale?](localedependentspeechmodule/supportedlocale(equivalentto:).md)
  A locale from the module’s supported locales equivalent to the given locale.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModule](speechmodule.md)
### Conforming Types
- [DictationTranscriber](dictationtranscriber.md)
- [SpeechTranscriber](speechtranscriber.md)

## See Also

- [protocol SpeechModule](speechmodule.md)
  Protocol that all analyzer modules conform to.
- [class SpeechTranscriber](speechtranscriber.md)
  A module that transcribes speech to text. This transcriber is appropriate for normal conversation and general purposes.
- [class DictationTranscriber](dictationtranscriber.md)
  A module that transcribes speech to text. This transcriber is used by `SFSpeechRecognizer` and system dictation features.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/localedependentspeechmodule)*