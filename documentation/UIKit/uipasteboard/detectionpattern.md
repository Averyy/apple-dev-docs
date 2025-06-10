# UIPasteboard.DetectionPattern

**Framework**: UIKit  
**Kind**: struct

An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
struct DetectionPattern
```

## Topics

### Detecting common patterns
- [static let number: UIPasteboard.DetectionPattern](uipasteboard/detectionpattern/number.md)
  A pattern that indicates the pasteboard contains a string that consists of a numeric value.
- [static let probableWebSearch: UIPasteboard.DetectionPattern](uipasteboard/detectionpattern/probablewebsearch.md)
  A pattern that indicates the pasteboard contains a string suitable for use as a web search term.
- [static let probableWebURL: UIPasteboard.DetectionPattern](uipasteboard/detectionpattern/probableweburl.md)
  A pattern that indicates the pasteboard contains a string that consists of a URL.
### Creating a detection pattern
- [init(rawValue: String)](uipasteboard/detectionpattern/init(rawvalue:).md)
  Creates a detection pattern to detect different types of content on the pasteboard.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<Set<PartialKeyPath<UIPasteboard.DetectedValues>>, any Error>) -> ())](uipasteboard/detectpatterns(for:completionhandler:)-23vwn.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>](uipasteboard/detectedpatterns(for:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[Set<PartialKeyPath<UIPasteboard.DetectedValues>>], any Error>) -> ())](uipasteboard/detectpatterns(for:initemset:completionhandler:)-7ubl1.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [Set<PartialKeyPath<UIPasteboard.DetectedValues>>]](uipasteboard/detectedpatterns(for:initemset:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<UIPasteboard.DetectedValues, any Error>) -> ())](uipasteboard/detectvalues(for:completionhandler:)-6adre.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> UIPasteboard.DetectedValues](uipasteboard/detectedvalues(for:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[UIPasteboard.DetectedValues], any Error>) -> ())](uipasteboard/detectvalues(for:initemset:completionhandler:)-pm9l.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [UIPasteboard.DetectedValues]](uipasteboard/detectedvalues(for:initemset:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [UIPasteboard.DetectedValues](uipasteboard/detectedvalues.md)
  An object that contains common types of data that the data detection system matches for a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectionpattern)*