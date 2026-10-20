# locale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The locale of the metadata item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var locale: Locale? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSLocale * locale;
```

#### Discussion

The locale may be `nil` if no locale information is available for the metadata item.

## See Also

### Accessing language support
- [var extendedLanguageTag: String?](./extendedlanguagetag.md)
  The IETF BCP 47 (RFC 4646) language identifier of the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/locale)*