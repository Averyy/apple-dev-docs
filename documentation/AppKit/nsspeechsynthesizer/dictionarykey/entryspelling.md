# entrySpelling

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The spelling of an entry. An `NSString`.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let entrySpelling: NSSpeechSynthesizer.DictionaryKey
```

```c
extern NSSpeechDictionaryKey const NSSpeechDictionaryEntrySpelling;
```

## See Also

### Type Properties
- [static let abbreviations: NSSpeechSynthesizer.DictionaryKey](./abbreviations.md)
  An array of dictionary objects containing the keys `NSSpeechDictionaryEntrySpelling` and `NSSpeechDictionaryEntryPhonemes`.
- [static let entryPhonemes: NSSpeechSynthesizer.DictionaryKey](./entryphonemes.md)
  The phonemic representation of an entry. An `NSString`.
- [static let localeIdentifier: NSSpeechSynthesizer.DictionaryKey](./localeidentifier.md)
  The canonical locale identifier string describing the dictionary’s locale.
- [static let modificationDate: NSSpeechSynthesizer.DictionaryKey](./modificationdate.md)
  A string representation of the dictionary’s last modification date in the international format (YYYY-MM-DD HH:MM:SS ±HHMM). If the same word appears across multiple dictionaries, the one from the dictionary with the most recent date will be used.
- [static let pronunciations: NSSpeechSynthesizer.DictionaryKey](./pronunciations.md)
  An array of dictionary objects containing the keys `NSSpeechDictionaryEntrySpelling` and `NSSpeechDictionaryEntryPhonemes`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/dictionarykey/entryspelling)*