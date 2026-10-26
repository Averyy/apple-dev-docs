# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The language tag of the track.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`extendedLanguageTag`](../avpartialasyncproperty/extendedlanguagetag.md) asynchronously instead.

## Declaration

```swift
var extendedLanguageTag: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * extendedLanguageTag;
```

#### Discussion

The value is a [BCP-47](https://tools.ietf.org/html/bcp47) language tag, or `nil` if the track doesn’t specify a language tag.

## See Also

### Accessing language support
- [languageCode](./languagecode.md)
  The language code of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/extendedlanguagetag)*