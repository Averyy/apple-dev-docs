# isEqual(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether the receiver is equal to the specified date interval.

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
func isEqual(to dateInterval: DateInterval) -> Bool
```

```objc
- (BOOL) isEqualToDateInterval:(NSDateInterval *) dateInterval;
```

#### Return Value

[`true`](../../Swift/true.md) if the [`startDate`](./startdate.md) and [`duration`](./duration.md) of `dateInterval` and the receiver are equal. Otherwise, [`false`](../../Swift/false.md).

## Parameters

- `dateInterval`: The date interval with which to check the receiver for equality.

## See Also

### Comparing Date Intervals
- [func compare(DateInterval) -> ComparisonResult](./compare%28_%29.md)
  Compares the receiver with the specified date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateinterval/isequal(to:))*