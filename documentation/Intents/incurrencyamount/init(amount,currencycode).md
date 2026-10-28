# init(amount:currencyCode:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a currency amount object with the specified values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(amount: NSDecimalNumber, currencyCode: String)
```

```objc
- (instancetype) initWithAmount:(NSDecimalNumber *) amount currencyCode:(NSString *) currencyCode;
```

## Return Value

An initialized currency amount object or `nil` if the object could not be created.

## Parameters

- `amount`: The decimal number representing the amount of money.
- `currencyCode`: The ISO 4217 currency code to apply to the specified `amount`. You can get a list of possible currency codes using the [`isoCurrencyCodes`](../../Foundation/nslocale/isocurrencycodes.md) method of [`NSLocale`](../../Foundation/nslocale.md). For example, the string “USD” corresponds to United States dollars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incurrencyamount/init(amount:currencycode:))*