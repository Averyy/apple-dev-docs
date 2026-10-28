# symbol

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The symbol used to represent the phoneme.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let symbol: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey
```

```c
extern NSSpeechPhonemeInfoKey const NSSpeechPhonemeInfoSymbol;
```

## Discussion

The symbol does not necessarily have a phonetic connection to the phoneme, but might simply be an abstract textual representation of it.

## See Also

### Phoneme Info Keys
- [static let example: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./example.md)
  An example word that illustrates the use of the phoneme.
- [static let hiliteEnd: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./hiliteend.md)
  The character offset into the example word that identifies the location of the end of the phoneme.
- [static let hiliteStart: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./hilitestart.md)
  The character offset into the example word that identifies the location of the beginning of the phoneme.
- [static let opcode: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./opcode.md)
  NSNumber


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/phonemeinfokey/symbol)*