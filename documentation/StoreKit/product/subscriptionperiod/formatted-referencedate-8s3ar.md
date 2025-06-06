# formatted(_:referenceDate:)

**Framework**: StoreKit  
**Kind**: method

Formats the subscription period using a format style that takes a duration as an input.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func formatted<S>(_ format: S, referenceDate: Date = .now) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Duration
```

## Parameters

- `format`: A format style that has a duration as an input.
- `referenceDate`: The starting date of the subscription period. The default value is  .

## See Also

- [func formatted<S>(S, referenceDate: Date) -> S.FormatOutput](product/subscriptionperiod/formatted(_:referencedate:)-3t7wd.md)
  Formats the subscription period using a format style that takes a date range as an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionperiod/formatted(_:referencedate:)-8s3ar)*