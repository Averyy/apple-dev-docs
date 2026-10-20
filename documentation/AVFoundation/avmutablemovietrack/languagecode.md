# languageCode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The language code of the track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var languageCode: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * languageCode;
```

#### Discussion

The value is an ISO 639-2/T language code, or `nil` if the track doesn’t specify a language code.

## See Also

### Accessing language support
- [var extendedLanguageTag: String?](./extendedlanguagetag.md)
  The language tag of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/languagecode)*