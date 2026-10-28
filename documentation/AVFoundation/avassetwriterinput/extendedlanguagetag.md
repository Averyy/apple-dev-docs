# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The extended language for the input’s track.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var extendedLanguageTag: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * extendedLanguageTag;
```

## Discussion

Extended language tags are normally set only when an ISO 639-2/T language code alone is ambiguous. For example, you may use an extended language tag to distinguish media by the regional dialect in use or the writing system employed.

Specify the value as an RFC 4646 language tag, or `nil` to prevent the writer from writing an extended language tag.

## See Also

### Configuring language support
- [var languageCode: String?](./languagecode.md)
  The language code of the input’s track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/extendedlanguagetag)*