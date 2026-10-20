# detectPatterns(for:inItemSet:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS

## Declaration

```swift
func detectPatterns(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet itemSet: IndexSet?, completionHandler: @escaping (Result<[Set<PartialKeyPath<UIPasteboard.DetectedValues>>], any Error>) -> ())
```

#### Discussion

Because this method only gives an indication of whether a pasteboard item matches a particular pattern and doesn’t allow the app to access the contents, the system doesn’t notify the user about reading the contents of the pasteboard.

## Parameters

- `keyPaths`: A set of key paths you use to indicate which types of patterns you want the data detection system to match.
- `itemSet`: A set of indexes you provide to indicate which pasteboard items the data detection system inspects to detect patterns.
- `completionHandler`: A closure you provide to process patterns the data detection system matches, or to handle errors.

## See Also

### Deprecated
- [Deprecated symbols](../uipasteboard-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<Set<PartialKeyPath<UIPasteboard.DetectedValues>>, any Error>) -> ())](./detectpatterns%28for,completionhandler%29-23vwn.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<UIPasteboard.DetectedValues, any Error>) -> ())](./detectvalues%28for,completionhandler%29-6adre.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectpatterns(for:initemset:completionhandler:)-7ubl1)*