# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The language tag of the track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var extendedLanguageTag: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * extendedLanguageTag;
```

#### Discussion

The value is a [BCP-47](https://tools.ietf.org/html/bcp47) language tag, or `nil` if the track doesn’t specify a language tag.

## See Also

### Accessing language support
- [var languageCode: String?](./languagecode.md)
  The language code of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/extendedlanguagetag)*