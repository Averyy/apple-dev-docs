# UIPasteboard.DetectionPattern

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * UIPasteboardDetectionPattern;
```

## Topics

### Detecting common patterns
- [static let number: UIPasteboard.DetectionPattern](./detectionpattern/number.md)
  A pattern that indicates the pasteboard contains a string that consists of a numeric value.
- [static let probableWebSearch: UIPasteboard.DetectionPattern](./detectionpattern/probablewebsearch.md)
  A pattern that indicates the pasteboard contains a string suitable for use as a web search term.
- [static let probableWebURL: UIPasteboard.DetectionPattern](./detectionpattern/probableweburl.md)
  A pattern that indicates the pasteboard contains a string that consists of a URL.
### Creating a detection pattern
- [init(rawValue: String)](./detectionpattern/init%28rawvalue%29.md)
  Creates a detection pattern to detect different types of content on the pasteboard.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Detecting patterns of content in pasteboard items
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>](./detectedpatterns%28for%29.md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [Set<PartialKeyPath<UIPasteboard.DetectedValues>>]](./detectedpatterns%28for,initemset%29.md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> UIPasteboard.DetectedValues](./detectedvalues%28for%29.md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[UIPasteboard.DetectedValues], any Error>) -> ())](./detectvalues%28for,initemset,completionhandler%29-pm9l.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [UIPasteboard.DetectedValues]](./detectedvalues%28for,initemset%29.md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [UIPasteboard.DetectedValues](./detectedvalues.md)
  An object that contains common types of data that the data detection system matches for a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectionpattern)*