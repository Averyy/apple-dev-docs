# amount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The monetary amount associated with the currency.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var amount: NSDecimalNumber? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDecimalNumber * amount;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDecimalNumber * amount;
```

## Discussion

This value in the [`currencyCode`](./currencycode.md) property determines the currency designator applied to this number.

## See Also

### Getting the Currency Information
- [var currencyCode: String?](./currencycode.md)
  The ISO 4217 currency code that applies to the monetary amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incurrencyamount/amount)*