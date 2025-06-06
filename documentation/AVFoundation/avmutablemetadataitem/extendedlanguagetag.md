# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property

The IETF BCP 47 (RFC 4646) language identifier of the metadata item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var extendedLanguageTag: String? { get set }
```

#### Discussion

The value may be `nil` if no language tag information is available.

## See Also

- [var locale: Locale?](avmutablemetadataitem/locale.md)
  The locale for a mutable metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/extendedlanguagetag)*