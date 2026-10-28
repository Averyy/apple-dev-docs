# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The language tag of the track.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var extendedLanguageTag: String? { get }
```

## Discussion

The value is a [BCP-47](https://tools.ietf.org/html/bcp47) language tag, or `nil` if the track doesn’t specify a language tag.

## See Also

### Accessing language support
- [var languageCode: String?](./languagecode.md)
  The language code of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack/extendedlanguagetag)*