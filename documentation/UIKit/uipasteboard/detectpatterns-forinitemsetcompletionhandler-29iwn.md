# detectPatterns(for:inItemSet:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Determines whether pasteboard items match the specified patterns, without notifying the user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
func detectPatterns(for patterns: Set<UIPasteboard.DetectionPattern>, inItemSet itemSet: IndexSet?, completionHandler: @escaping (Result<[Set<UIPasteboard.DetectionPattern>], any Error>) -> ())
```

#### Discussion

Because this method only detects for the presence of patterns and does not read the contents of the pasteboard, the system doesn’t notify the user about reading the contents of the pasteboard.

## Parameters

- `patterns`: The patterns to detect on the pasteboard.
- `itemSet`: An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass   to detect patterns in all pasteboard items.
- `completionHandler`: A closure that the system invokes after detecting patterns on the pasteboard. The closure receives a   instance that contains either an array with the patterns found on the pasteboard or an error if detection failed. If the   instance contains an array, the index of each element in the array corresponds to the pasteboard item index specified in  .

## See Also

- [var isPersistent: Bool](uipasteboard/ispersistent.md)
  A Boolean value that indicates whether the pasteboard is persistent.
- [func setPersistent(Bool)](uipasteboard/setpersistent(_:).md)
  A Boolean value that indicates whether the pasteboard is persistent.
- [func detectPatterns(for: Set<UIPasteboard.DetectionPattern>, completionHandler: (Result<Set<UIPasteboard.DetectionPattern>, any Error>) -> ())](uipasteboard/detectpatterns(for:completionhandler:)-5zlnd.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the user.
- [func detectValues(for: Set<UIPasteboard.DetectionPattern>, completionHandler: (Result<[UIPasteboard.DetectionPattern : Any], any Error>) -> ())](uipasteboard/detectvalues(for:completionhandler:)-9p2ff.md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [func detectValues(for: Set<UIPasteboard.DetectionPattern>, inItemSet: IndexSet?, completionHandler: (Result<[[UIPasteboard.DetectionPattern : Any]], any Error>) -> ())](uipasteboard/detectvalues(for:initemset:completionhandler:)-8y0iw.md)
  Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectpatterns(for:initemset:completionhandler:)-29iwn)*