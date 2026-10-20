# progress

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Set when the Block is called to report progress during a long-running match operation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var progress: NSRegularExpression.MatchingFlags { get }
```

```c
NSMatchingProgress
```

## See Also

### Constants
- [static var completed: NSRegularExpression.MatchingFlags](./completed.md)
  Set when the Block is called after matching has completed.
- [static var hitEnd: NSRegularExpression.MatchingFlags](./hitend.md)
  Set when the current match operation reached the end of the search range.
- [static var requiredEnd: NSRegularExpression.MatchingFlags](./requiredend.md)
  Set when the current match depended on the location of the end of the search range.
- [static var internalError: NSRegularExpression.MatchingFlags](./internalerror.md)
  Set when matching failed due to an internal error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/matchingflags/progress)*