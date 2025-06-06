# isPersistent

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the pasteboard is persistent.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isPersistent: Bool { get }
```

#### Discussion

Nonpersistent named pasteboards remain available. You can use these to implement such features as Duplicate or Copy Style. A nonpersistent named pasteboard is available only in the process that creates it.

## See Also

- [init?(name: UIPasteboard.Name, create: Bool)](uipasteboard/init(name:create:).md)
  Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [class func withUniqueName() -> UIPasteboard](uipasteboard/withuniquename.md)
  Returns an app pasteboard that you identify by a unique system-generated name.
- [func setPersistent(Bool)](uipasteboard/setpersistent(_:).md)
  A Boolean value that indicates whether the pasteboard is persistent.
- [func detectPatterns(for: Set<UIPasteboard.DetectionPattern>, completionHandler: (Result<Set<UIPasteboard.DetectionPattern>, any Error>) -> ())](uipasteboard/detectpatterns(for:completionhandler:)-5zlnd.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the user.
- [func detectPatterns(for: Set<UIPasteboard.DetectionPattern>, inItemSet: IndexSet?, completionHandler: (Result<[Set<UIPasteboard.DetectionPattern>], any Error>) -> ())](uipasteboard/detectpatterns(for:initemset:completionhandler:)-29iwn.md)
  Determines whether pasteboard items match the specified patterns, without notifying the user.
- [func detectValues(for: Set<UIPasteboard.DetectionPattern>, completionHandler: (Result<[UIPasteboard.DetectionPattern : Any], any Error>) -> ())](uipasteboard/detectvalues(for:completionhandler:)-9p2ff.md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [func detectValues(for: Set<UIPasteboard.DetectionPattern>, inItemSet: IndexSet?, completionHandler: (Result<[[UIPasteboard.DetectionPattern : Any]], any Error>) -> ())](uipasteboard/detectvalues(for:initemset:completionhandler:)-8y0iw.md)
  Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/ispersistent)*