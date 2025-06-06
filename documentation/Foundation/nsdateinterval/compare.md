# compare(_:)

**Framework**: Foundation  
**Kind**: method

Compares the receiver with the specified date interval.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func compare(_ dateInterval: DateInterval) -> ComparisonResult
```

#### Return Value

Returns an [`ComparisonResult`](comparisonresult.md) value that indicates the temporal ordering of the receiver and a given date interval:

- [`ComparisonResult.orderedAscending`](comparisonresult/orderedascending.md) if the receiver’s [`startDate`](nsdateinterval/startdate.md) occurs earlier than that of `dateInterval`, or both [`startDate`](nsdateinterval/startdate.md) values are equal and the [`duration`](nsdateinterval/duration.md) of the receiver is less than that of `dateInterval`.
- [`ComparisonResult.orderedDescending`](comparisonresult/ordereddescending.md) if the receiver’s [`startDate`](nsdateinterval/startdate.md) occurs later than that of `dateInterval`, or both [`startDate`](nsdateinterval/startdate.md) values are equal and the [`duration`](nsdateinterval/duration.md) of the receiver is greater than that of `dateInterval`.
- [`ComparisonResult.orderedSame`](comparisonresult/orderedsame.md) if the receiver’s [`startDate`](nsdateinterval/startdate.md) and [`duration`](nsdateinterval/duration.md) values are equal to those of `dateInterval`.

#### Discussion

The following figure illustrates four `NSDateInterval` objects plotted on an arbitrary time axis. Each date interval spans its [`duration`](nsdateinterval/duration.md) from left to right, from its [`startDate`](nsdateinterval/startdate.md) to its [`endDate`](nsdateinterval/enddate.md).

![None](https://docs-assets.developer.apple.com/published/62f0900557039aff36d72008ce7f3ba3/media-2556955%402x.png)

The result of comparing the date interval labeled  with the date interval labeled  is [`ComparisonResult.orderedAscending`](comparisonresult/orderedascending.md), because  has a [`startDate`](nsdateinterval/startdate.md) that occurs earlier than that of .

The result of comparing the date interval labeled  with the date interval labeled  is [`ComparisonResult.orderedDescending`](comparisonresult/ordereddescending.md), because because  and  have the same [`startDate`](nsdateinterval/startdate.md), and  has a [`duration`](nsdateinterval/duration.md) greater than that of .

## Parameters

- `dateInterval`: The date interval with which to compare the receiver.

## See Also

- [func isEqual(to: DateInterval) -> Bool](nsdateinterval/isequal(to:).md)
  Indicates whether the receiver is equal to the specified date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateinterval/compare(_:))*