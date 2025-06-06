# isISOLanguage

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether this language code is in the list of ISO-defined languages.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isISOLanguage: Bool { get }
```

#### Discussion

The following code snippet illustrates use of the [`isISOLanguage`](locale/languagecode-swift.struct/isisolanguage.md) value.

```swift
let enIsISO = Locale.LanguageCode("en").isISOLanguage // true
let gibberishIsISO = Locale.LanguageCode("gibberish").isISOLanguage // false
```

## See Also

- [var identifier: String](locale/languagecode-swift.struct/identifier.md)
  The identifier used to create the language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/languagecode-swift.struct/isisolanguage)*