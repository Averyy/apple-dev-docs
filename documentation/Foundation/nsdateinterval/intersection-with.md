# intersection(with:)

**Framework**: Foundation  
**Kind**: method

Returns the intersection between the receiver and the specified date interval.

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
func intersection(with dateInterval: DateInterval) -> DateInterval?
```

#### Return Value

A date interval for the intersection of the receiver and `dateInterval`, or `nil` if no intersection occurs.

#### Discussion

Calculating the intersection of date intervals is a commutative and associative operation. The intersection of a date interval with itself is equal to itself.

The following figure illustrates five `NSDateInterval` objects plotted on an arbitrary time axis. Each date interval spans its [`duration`](nsdateinterval/duration.md) from left to right, from its [`startDate`](nsdateinterval/startdate.md) to its [`endDate`](nsdateinterval/enddate.md).

![None](https://docs-assets.developer.apple.com/published/f85a09eb2c779e75f6979bf07902e8e3/media-2556958%402x.png)

The date intervals labeled  and  do not intersect, because the [`startDate`](nsdateinterval/startdate.md) of  occurs later than the [`endDate`](nsdateinterval/enddate.md) of .

The date intervals  labeled  and  do intersect. The date interval labeled  represents the result of calculating the intersection between  and .

## Parameters

- `dateInterval`: The date interval with which to calculate the intersection of the receiver.

## See Also

- [func intersects(DateInterval) -> Bool](nsdateinterval/intersects(_:).md)
  Indicates whether the receiver intersects with the specified date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateinterval/intersection(with:))*