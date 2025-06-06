# languageCode

**Framework**: AVFoundation  
**Kind**: property

The language code of the track.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var languageCode: AVAsyncProperty<Root, String?> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

The value is an ISO 639-2/T language code, or `nil` if the track doesn’t specify a language code.

## See Also

- [static var extendedLanguageTag: AVAsyncProperty<Root, String?>](avpartialasyncproperty/extendedlanguagetag.md)
  The language tag of the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/languagecode)*