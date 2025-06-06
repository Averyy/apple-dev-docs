# number

**Framework**: UIKit  
**Kind**: property

A pattern that indicates the pasteboard contains a string that consists of a numeric value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
static let number: UIPasteboard.DetectionPattern
```

#### Discussion

When you include this pattern in calls to [`detectValues(for:inItemSet:completionHandler:)`](uipasteboard/detectvalues(for:initemset:completionhandler:)-pm9l.md) or [`detectValues(for:completionHandler:)`](uipasteboard/detectvalues(for:completionhandler:)-6adre.md) — [`detectValuesForPatterns:inItemSet:completionHandler:`](uipasteboard/detectvaluesforpatterns:initemset:completionhandler:.md) or [`detectValuesForPatterns:completionHandler:`](uipasteboard/detectvaluesforpatterns:completionhandler:.md) in Objective-C — and the pasteboard detects a number, it reports the value as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).

## See Also

- [static let probableWebSearch: UIPasteboard.DetectionPattern](uipasteboard/detectionpattern/probablewebsearch.md)
  A pattern that indicates the pasteboard contains a string suitable for use as a web search term.
- [static let probableWebURL: UIPasteboard.DetectionPattern](uipasteboard/detectionpattern/probableweburl.md)
  A pattern that indicates the pasteboard contains a string that consists of a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectionpattern/number)*