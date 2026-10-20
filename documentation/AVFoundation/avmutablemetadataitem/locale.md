# locale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The locale for a mutable metadata item.

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
var locale: Locale? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSLocale * locale;
```

#### Discussion

The locale may be `nil` if no locale information is available for the item.

## See Also

### Accessing language support
- [var extendedLanguageTag: String?](./extendedlanguagetag.md)
  The IETF BCP 47 (RFC 4646) language identifier of the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/locale)*