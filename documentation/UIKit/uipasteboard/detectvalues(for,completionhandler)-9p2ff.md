# detectValues(for:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.

**Availability**:
- iOS 14.0+ - Deprecated in 15.0
- iPadOS 14.0+ - Deprecated in 15.0
- Mac Catalyst 14.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`detectValues(for:completionHandler:)`](./detectvalues%28for,completionhandler%29-6adre.md) instead.

## Declaration

```swift
func detectValues(for patterns: Set<UIPasteboard.DetectionPattern>, completionHandler: @escaping (Result<[UIPasteboard.DetectionPattern : Any], any Error>) -> ())
```

## Discussion

> ❗ **Important**:  Calling this method notifies the user that the app has read the contents of the pasteboard.

For details about the types returned for each pattern, see [`UIPasteboard.DetectionPattern`](./detectionpattern.md).

## Parameters

- `patterns`: The patterns to detect on the pasteboard.
- `completionHandler`: A closure that the system invokes after detecting patterns on the pasteboard. The closure receives a `Result` instance that contains either a dictionary with the patterns found on the pasteboard or an error if detection failed. If the `Result` instance contains a dictionary, the keys specify the matched pattern, and the value specifies the content of the pasteboard.

## See Also

### Deprecated
- [var isPersistent: Bool](./ispersistent.md)
  A Boolean value that indicates whether the pasteboard is persistent.
- [func setPersistent(Bool)](./setpersistent%28_%29.md)
  A Boolean value that indicates whether the pasteboard is persistent.
- [func detectPatterns(for: Set<UIPasteboard.DetectionPattern>, completionHandler: (Result<Set<UIPasteboard.DetectionPattern>, any Error>) -> ())](./detectpatterns%28for,completionhandler%29-5zlnd.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the user.
- [func detectPatterns(for: Set<UIPasteboard.DetectionPattern>, inItemSet: IndexSet?, completionHandler: (Result<[Set<UIPasteboard.DetectionPattern>], any Error>) -> ())](./detectpatterns%28for,initemset,completionhandler%29-29iwn.md)
  Determines whether pasteboard items match the specified patterns, without notifying the user.
- [func detectValues(for: Set<UIPasteboard.DetectionPattern>, inItemSet: IndexSet?, completionHandler: (Result<[[UIPasteboard.DetectionPattern : Any]], any Error>) -> ())](./detectvalues%28for,initemset,completionhandler%29-8y0iw.md)
  Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectvalues(for:completionhandler:)-9p2ff)*