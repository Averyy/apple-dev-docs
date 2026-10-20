# union(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Returns a new time range with the time elements of both this time range and the given time range.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
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

### Combining Time Ranges
- [func intersection(CMTimeRange) -> CMTimeRange](./intersection%28_%29.md)
  Returns a new time range with the time elements that are common to both this time range and the given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange/union(_:))*