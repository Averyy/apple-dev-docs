# init(price:currencyCode:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the object with the specified price information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
convenience init(price: NSDecimalNumber, currencyCode: String)
```

```objc
- (instancetype) initWithPrice:(NSDecimalNumber *) price currencyCode:(NSString *) currencyCode;
```

## Return Value

An initialized price range object or `nil` if the object could not be created.

## Discussion

This method sets the [`minimumPrice`](./minimumprice.md) and [`maximumPrice`](./maximumprice.md) properties to the value in the `price` parameter.

## Parameters

- `price`: The price of the service. This value is used for both the minimum and maximum prices.
- `currencyCode`: The ISO 4217 currency code to apply to the price information. You can get a list of possible currency codes using the [`isoCurrencyCodes`](../../Foundation/nslocale/isocurrencycodes.md) method of [`NSLocale`](../../Foundation/nslocale.md). For example, the string “USD” corresponds to United States dollars.

## See Also

### Creating a Price Range Object
- [init(firstPrice: NSDecimalNumber, secondPrice: NSDecimalNumber, currencyCode: String)](./init%28firstprice,secondprice,currencycode%29.md)
  Initializes the object with the specified range of prices.
- [init(maximumPrice: NSDecimalNumber, currencyCode: String)](./init%28maximumprice,currencycode%29.md)
  Initializes the object with the specified maximum price information.
- [init(minimumPrice: NSDecimalNumber, currencyCode: String)](./init%28minimumprice,currencycode%29.md)
  Initializes the object with the specified minimum price information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpricerange/init(price:currencycode:))*