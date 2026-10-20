# pronunciations

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An array of dictionary objects containing the keys `NSSpeechDictionaryEntrySpelling` and `NSSpeechDictionaryEntryPhonemes`.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let pronunciations: NSSpeechSynthesizer.DictionaryKey
```

```c
extern NSSpeechDictionaryKey const NSSpeechDictionaryPronunciations;
```

## See Also

### Type Properties
- [static let abbreviations: NSSpeechSynthesizer.DictionaryKey](./abbreviations.md)
  An array of dictionary objects containing the keys `NSSpeechDictionaryEntrySpelling` and `NSSpeechDictionaryEntryPhonemes`.
- [static let entryPhonemes: NSSpeechSynthesizer.DictionaryKey](./entryphonemes.md)
  The phonemic representation of an entry. An `NSString`.
- [static let entrySpelling: NSSpeechSynthesizer.DictionaryKey](./entryspelling.md)
  The spelling of an entry. An `NSString`.
- [static let localeIdentifier: NSSpeechSynthesizer.DictionaryKey](./localeidentifier.md)
  The canonical locale identifier string describing the dictionary’s locale.
- [static let modificationDate: NSSpeechSynthesizer.DictionaryKey](./modificationdate.md)
  A string representation of the dictionary’s last modification date in the international format (YYYY-MM-DD HH:MM:SS ±HHMM). If the same word appears across multiple dictionaries, the one from the dictionary with the most recent date will be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/dictionarykey/pronunciations)*