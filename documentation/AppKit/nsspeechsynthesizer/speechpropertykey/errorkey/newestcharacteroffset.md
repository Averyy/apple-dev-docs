# newestCharacterOffset

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The position in the text string of the most recent error that occurred since the last call to [`object(forProperty:)`](../../object%28forproperty%29.md) with the [`errors`](../errors.md) property. An `NSNumber`.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let newestCharacterOffset: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey
```

```c
extern NSSpeechErrorKey const NSSpeechErrorNewestCharacterOffset;
```

## See Also

### Type Properties
- [static let count: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](./count.md)
  The number of errors that have occurred in processing the current text string, since the last call to [`object(forProperty:)`](../../object%28forproperty%29.md) with the [`errors`](../errors.md) property.  An `NSNumber`
- [static let newestCode: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](./newestcode.md)
  The error code of the most recent error that occurred since the last call to [`object(forProperty:)`](../../object%28forproperty%29.md) with the [`errors`](../errors.md) property.  An `NSNumber`
- [static let oldestCharacterOffset: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](./oldestcharacteroffset.md)
  The position in the text string of the first error that occurred since the last call to [`object(forProperty:)`](../../object%28forproperty%29.md) with the [`errors`](../errors.md) property.  An `NSNumber`
- [static let oldestCode: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](./oldestcode.md)
  The error code of the first error that occurred since the last call to [`object(forProperty:)`](../../object%28forproperty%29.md) with the [`errors`](../errors.md) property.  An `NSNumber`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/errorkey/newestcharacteroffset)*