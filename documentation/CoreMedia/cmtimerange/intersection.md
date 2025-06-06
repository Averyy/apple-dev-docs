# intersection(_:)

**Framework**: Core Media  
**Kind**: method

Returns a new time range with the time elements that are common to both this time range and the given time range.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst ?+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func intersection(_ otherRange: CMTimeRange) -> CMTimeRange
```

#### Return Value

A time range that represents the largest intersection of the input.

## Parameters

- `otherRange`: A time range to intersect.

## See Also

- [func union(CMTimeRange) -> CMTimeRange](cmtimerange/union(_:).md)
  Returns a new time range with the time elements of both this time range and the given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange/intersection(_:))*