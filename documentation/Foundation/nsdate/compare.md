# compare(_:)

**Framework**: Foundation  
**Kind**: method

Indicates the temporal ordering of the receiver and another given date.

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
func compare(_ other: Date) -> ComparisonResult
```

#### Return Value

If:

- The receiver and `anotherDate` are exactly equal to each other, [`ComparisonResult.orderedSame`](comparisonresult/orderedsame.md)
- The receiver is later in time than `anotherDate`, [`ComparisonResult.orderedDescending`](comparisonresult/ordereddescending.md)
- The receiver is earlier in time than `anotherDate`, [`ComparisonResult.orderedAscending`](comparisonresult/orderedascending.md).

#### Discussion

This method detects sub-second differences between dates. If you want to compare dates with a less fine granularity, use [`timeIntervalSince(_:)`](nsdate/timeintervalsince(_:).md) to compare the two dates.

## Parameters

- `other`: This value must not be  . If the value is  , the behavior is undefined and may change in future versions of macOS.

## See Also

- [func isEqual(_ object: Any?) -> Bool](../ObjectiveC/NSObjectProtocol/isEqual(_:).md)
  Returns a Boolean value that indicates whether the receiver and a given object are equal.
- [func isEqual(to: Date) -> Bool](nsdate/isequal(to:).md)
  Returns a Boolean value that indicates whether a given object is a date that is exactly equal the receiver.
- [func earlierDate(Date) -> Date](nsdate/earlierdate(_:).md)
  Returns the earlier of the receiver and another given date.
- [func laterDate(Date) -> Date](nsdate/laterdate(_:).md)
  Returns the later of the receiver and another given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/compare(_:))*