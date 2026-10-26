# languageCode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The language code of the track.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`languageCode`](../avpartialasyncproperty/languagecode.md) asynchronously instead.

## Declaration

```swift
var languageCode: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * languageCode;
```

#### Discussion

The value is an ISO 639-2/T language code, or `nil` if the track doesn’t specify a language code.

## See Also

### Accessing language support
- [extendedLanguageTag](./extendedlanguagetag.md)
  The language tag of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/languagecode)*