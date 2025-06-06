# union(_:)

**Framework**: Core Media  
**Kind**: method

Returns a new time range with the time elements of both this time range and the given time range.

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
func union(_ otherRange: CMTimeRange) -> CMTimeRange
```

#### Return Value

A time range with the unique time elements of this time range and the input.

## Parameters

- `otherRange`: A time range.

## See Also

- [func intersection(CMTimeRange) -> CMTimeRange](cmtimerange/intersection(_:).md)
  Returns a new time range with the time elements that are common to both this time range and the given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange/union(_:))*