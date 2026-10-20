# CMTimeRange

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

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

```c
typedef struct { ... } CMTimeRange;
```

## Topics

### Creating Time Ranges
- [init()](./cmtimerange/init%28%29.md)
  Creates an empty time range at zero.
- [init(start: CMTime, duration: CMTime)](./cmtimerange/init%28start,duration%29.md)
  Creates a valid time range with a start time and duration.
- [init(start: CMTime, end: CMTime)](./cmtimerange/init%28start,end%29.md)
  Creates a valid time range from a start and end time.
### Inspecting Time Ranges
- [var start: CMTime](./cmtimerange/start.md)
  The start time of the time range.
- [var end: CMTime](./cmtimerange/end.md)
  The end time of the time range.
- [var duration: CMTime](./cmtimerange/duration.md)
  The duration of the time range.
- [var isValid: Bool](./cmtimerange/isvalid.md)
  A Boolean value that indicates whether the time range is valid.
- [var isEmpty: Bool](./cmtimerange/isempty.md)
  A Boolean value that indicates whether the time range is empty.
- [var isIndefinite: Bool](./cmtimerange/isindefinite.md)
  A Boolean value that indicates whether the time range is indefinite.
### Finding Elements
- [func containsTime(CMTime) -> Bool](./cmtimerange/containstime%28_%29.md)
  Returns a Boolean value that indicates whether the time range contains a time.
- [func containsTimeRange(CMTimeRange) -> Bool](./cmtimerange/containstimerange%28_%29.md)
  Returns a Boolean value that indicates whether the time range contains another time range.
### Combining Time Ranges
- [func intersection(CMTimeRange) -> CMTimeRange](./cmtimerange/intersection%28_%29.md)
  Returns a new time range with the time elements that are common to both this time range and the given time range.
- [func union(CMTimeRange) -> CMTimeRange](./cmtimerange/union%28_%29.md)
  Returns a new time range with the time elements of both this time range and the given time range.
### Constants
- [static let zero: CMTimeRange](./cmtimerange/zero.md)
  A constant for generating an empty time range at zero.
- [static let invalid: CMTimeRange](./cmtimerange/invalid.md)
  A constant for generating an invalid time range.
### Operators
- [static func != (CMTimeRange, CMTimeRange) -> Bool](./cmtimerange/noteq%28_,_%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange)*