# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property

The language tag of the track.

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
var extendedLanguageTag: String? { get }
```

#### Discussion

The value is a [`BCP-47`](https://developer.apple.comhttps://tools.ietf.org/html/bcp47) language tag, or `nil` if the track doesn’t specify a language tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/extendedlanguagetag)*