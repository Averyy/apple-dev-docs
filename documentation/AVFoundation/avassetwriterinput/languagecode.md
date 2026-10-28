# languageCode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The language code of the input’s track.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var languageCode: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * languageCode;
```

## Discussion

Specify an ISO 639-2/T language code value, or `nil` to prevent the writer from writing a language code.

## See Also

### Configuring language support
- [var extendedLanguageTag: String?](./extendedlanguagetag.md)
  The extended language for the input’s track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/languagecode)*