# oldestCharacterOffset

**Framework**: AppKit  
**Kind**: property

The position in the text string of the first error that occurred since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property.  An `NSNumber`

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let oldestCharacterOffset: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey
```

## See Also

- [static let count: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey/count.md)
  The number of errors that have occurred in processing the current text string, since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property.  An `NSNumber`
- [static let newestCharacterOffset: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey/newestcharacteroffset.md)
  The position in the text string of the most recent error that occurred since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property. An `NSNumber`.
- [static let newestCode: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey/newestcode.md)
  The error code of the most recent error that occurred since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property.  An `NSNumber`
- [static let oldestCode: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey/oldestcode.md)
  The error code of the first error that occurred since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property.  An `NSNumber`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/errorkey/oldestcharacteroffset)*