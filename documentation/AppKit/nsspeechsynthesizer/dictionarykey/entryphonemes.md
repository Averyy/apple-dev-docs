# entryPhonemes

**Framework**: AppKit  
**Kind**: property

The phonemic representation of an entry. An `NSString`.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let entryPhonemes: NSSpeechSynthesizer.DictionaryKey
```

## See Also

- [static let abbreviations: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/abbreviations.md)
  An array of dictionary objects containing the keys [`entrySpelling`](nsspeechsynthesizer/dictionarykey/entryspelling.md) and [`entryPhonemes`](nsspeechsynthesizer/dictionarykey/entryphonemes.md).
- [static let entrySpelling: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/entryspelling.md)
  The spelling of an entry. An `NSString`.
- [static let localeIdentifier: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/localeidentifier.md)
  The canonical locale identifier string describing the dictionary’s locale. A locale is generally composed of three pieces of ordered information: a language code, a region code, and a variant code.  Refer to documentation about [`NSLocale`](https://developer.apple.com/documentation/Foundation/NSLocale) or [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i) for more information
- [static let modificationDate: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/modificationdate.md)
  A string representation of the dictionary’s last modification date in the international format (YYYY-MM-DD HH:MM:SS ±HHMM). If the same word appears across multiple dictionaries, the one from the dictionary with the most recent date will be used.
- [static let pronunciations: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/pronunciations.md)
  An array of dictionary objects containing the keys [`entrySpelling`](nsspeechsynthesizer/dictionarykey/entryspelling.md) and [`entryPhonemes`](nsspeechsynthesizer/dictionarykey/entryphonemes.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/dictionarykey/entryphonemes)*