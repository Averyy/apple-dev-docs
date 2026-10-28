# detectedPatterns(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS

## Declaration

```swift
func detectedPatterns(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>
```

## Return Value

A set of key paths that represent the patterns the data detection system matches in the pasteboard.

## Discussion

Because this method only gives an indication of whether a pasteboard item matches a particular pattern and doesn’t allow the app to access the contents, the system doesn’t notify the user about reading the contents of the pasteboard.

## Parameters

- `keyPaths`: A set of key paths you use to indicate which types of patterns you want the data detection system to match.

## See Also

### Detecting patterns of content in pasteboard items
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
- [UIPasteboard.DetectionPattern](./detectionpattern.md)
  An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectedpatterns(for:))*