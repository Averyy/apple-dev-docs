# LocaleDependentSpeechModule

**Framework**: Speech  
**Kind**: protocol

A module that requires locale-specific assets.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol LocaleDependentSpeechModule : SpeechModule
```

## Topics

### Getting supported locales
- [static var supportedLocales: [Locale]](localedependentspeechmodule/supportedlocales.md)
  The set of all possible asset locales that the module supports.
- [static func supportedLocale(equivalentTo: Locale) async -> Locale?](localedependentspeechmodule/supportedlocale(equivalentto:).md)
  A locale from the module’s supported locales equivalent to the given locale.
### Inspecting an instance’s locales
- [var selectedLocales: [Locale]](localedependentspeechmodule/selectedlocales.md)
  The set of asset locales specified by the module’s configuration.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModule](speechmodule.md)
### Conforming Types
- [DictationTranscriber](dictationtranscriber.md)
- [SpeechTranscriber](speechtranscriber.md)

## See Also

- [class SpeechTranscriber](speechtranscriber.md)
  A speech-to-text transcription module that’s appropriate for normal conversation and general purposes.
- [class DictationTranscriber](dictationtranscriber.md)
  A speech-to-text transcription module that’s similar to system dictation features and compatible with older devices.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.
- [protocol SpeechModule](speechmodule.md)
  Protocol that all analyzer modules conform to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/localedependentspeechmodule)*