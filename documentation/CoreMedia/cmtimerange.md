# CMTimeRange

**Framework**: Core Media  
**Kind**: struct

A structure that represents a time range.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct CMTimeRange
```

## Topics

### Creating Time Ranges
- [init()](cmtimerange/init.md)
  Creates an empty time range at zero.
- [init(start: CMTime, duration: CMTime)](cmtimerange/init(start:duration:).md)
  Creates a valid time range with a start time and duration.
- [init(start: CMTime, end: CMTime)](cmtimerange/init(start:end:).md)
  Creates a valid time range from a start and end time.
### Inspecting Time Ranges
- [var start: CMTime](cmtimerange/start.md)
  The start time of the time range.
- [var end: CMTime](cmtimerange/end.md)
  The end time of the time range.
- [var duration: CMTime](cmtimerange/duration.md)
  The duration of the time range.
- [var isValid: Bool](cmtimerange/isvalid.md)
  A Boolean value that indicates whether the time range is valid.
- [var isEmpty: Bool](cmtimerange/isempty.md)
  A Boolean value that indicates whether the time range is empty.
- [var isIndefinite: Bool](cmtimerange/isindefinite.md)
  A Boolean value that indicates whether the time range is indefinite.
### Finding Elements
- [func containsTime(CMTime) -> Bool](cmtimerange/containstime(_:).md)
  Returns a Boolean value that indicates whether the time range contains a time.
- [func containsTimeRange(CMTimeRange) -> Bool](cmtimerange/containstimerange(_:).md)
  Returns a Boolean value that indicates whether the time range contains another time range.
### Combining Time Ranges
- [func intersection(CMTimeRange) -> CMTimeRange](cmtimerange/intersection(_:).md)
  Returns a new time range with the time elements that are common to both this time range and the given time range.
- [func union(CMTimeRange) -> CMTimeRange](cmtimerange/union(_:).md)
  Returns a new time range with the time elements of both this time range and the given time range.
### Constants
- [static let zero: CMTimeRange](cmtimerange/zero.md)
  A constant for generating an empty time range at zero.
- [static let invalid: CMTimeRange](cmtimerange/invalid.md)
  A constant for generating an invalid time range.
### Operators
- [static func != (CMTimeRange, CMTimeRange) -> Bool](cmtimerange/!=(_:_:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange)*