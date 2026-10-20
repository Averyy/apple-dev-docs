# compare(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSComparisonResult) compare:(NSDateInterval *) dateInterval;
```

#### Return Value

Returns an [`ComparisonResult`](../comparisonresult.md) value that indicates the temporal ordering of the receiver and a given date interval:

- [`ComparisonResult.orderedAscending`](../comparisonresult/orderedascending.md) if the receiver’s [`startDate`](./startdate.md) occurs earlier than that of `dateInterval`, or both [`startDate`](./startdate.md) values are equal and the [`duration`](./duration.md) of the receiver is less than that of `dateInterval`.
- [`ComparisonResult.orderedDescending`](../comparisonresult/ordereddescending.md) if the receiver’s [`startDate`](./startdate.md) occurs later than that of `dateInterval`, or both [`startDate`](./startdate.md) values are equal and the [`duration`](./duration.md) of the receiver is greater than that of `dateInterval`.
- [`ComparisonResult.orderedSame`](../comparisonresult/orderedsame.md) if the receiver’s [`startDate`](./startdate.md) and [`duration`](./duration.md) values are equal to those of `dateInterval`.

#### Discussion

The following figure illustrates four `NSDateInterval` objects plotted on an arbitrary time axis. Each date interval spans its [`duration`](./duration.md) from left to right, from its [`startDate`](./startdate.md) to its [`endDate`](./enddate.md).

![](https://developer.apple.com/tutorials/images/com.apple.foundation/media-2556955@2x.png)

The result of comparing the date interval labeled **A** with the date interval labeled **B** is [`ComparisonResult.orderedAscending`](../comparisonresult/orderedascending.md), because **A** has a [`startDate`](./startdate.md) that occurs earlier than that of **B**.

The result of comparing the date interval labeled **C** with the date interval labeled **D** is [`ComparisonResult.orderedDescending`](../comparisonresult/ordereddescending.md), because because **C** and **D** have the same [`startDate`](./startdate.md), and **C** has a [`duration`](./duration.md) greater than that of **D**.

## Parameters

- `dateInterval`: The date interval with which to compare the receiver.

## See Also

### Comparing Date Intervals
- [func isEqual(to: DateInterval) -> Bool](./isequal%28to%29.md)
  Indicates whether the receiver is equal to the specified date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateinterval/compare(_:))*