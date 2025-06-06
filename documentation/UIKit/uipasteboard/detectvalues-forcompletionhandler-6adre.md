# detectValues(for:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func detectValues(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: @escaping (Result<UIPasteboard.DetectedValues, any Error>) -> ())
```

#### Discussion

Because this method gives the app access to the values it detects in the pasteboard, the system notifies the user about reading the contents of the pasteboard.

## Parameters

- `keyPaths`: A set of key paths you use to indicate which types of data you want the data detection system to match.
- `completionHandler`: A closure you provide to process data the data detection system matches, or to handle errors.

## See Also

- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<Set<PartialKeyPath<UIPasteboard.DetectedValues>>, any Error>) -> ())](uipasteboard/detectpatterns(for:completionhandler:)-23vwn.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>](uipasteboard/detectedpatterns(for:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[Set<PartialKeyPath<UIPasteboard.DetectedValues>>], any Error>) -> ())](uipasteboard/detectpatterns(for:initemset:completionhandler:)-7ubl1.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [Set<PartialKeyPath<UIPasteboard.DetectedValues>>]](uipasteboard/detectedpatterns(for:initemset:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> UIPasteboard.DetectedValues](uipasteboard/detectedvalues(for:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[UIPasteboard.DetectedValues], any Error>) -> ())](uipasteboard/detectvalues(for:initemset:completionhandler:)-pm9l.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [UIPasteboard.DetectedValues]](uipasteboard/detectedvalues(for:initemset:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [UIPasteboard.DetectedValues](uipasteboard/detectedvalues.md)
  An object that contains common types of data that the data detection system matches for a pasteboard.
- [UIPasteboard.DetectionPattern](uipasteboard/detectionpattern.md)
  An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectvalues(for:completionhandler:)-6adre)*