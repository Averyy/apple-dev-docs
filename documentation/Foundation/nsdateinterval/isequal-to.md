# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the [`startDate`](nsdateinterval/startdate.md) and [`duration`](nsdateinterval/duration.md) of `dateInterval` and the receiver are equal. Otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `dateInterval`: The date interval with which to check the receiver for equality.

## See Also

- [func compare(DateInterval) -> ComparisonResult](nsdateinterval/compare(_:).md)
  Compares the receiver with the specified date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateinterval/isequal(to:))*