# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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
var extendedLanguageTag: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * extendedLanguageTag;
```

#### Discussion

The value may be `nil` if no language tag information is available.

## See Also

### Accessing language support
- [var locale: Locale?](./locale.md)
  The locale of the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/extendedlanguagetag)*