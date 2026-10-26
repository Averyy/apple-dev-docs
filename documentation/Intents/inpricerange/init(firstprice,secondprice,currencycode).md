# init(firstPrice:secondPrice:currencyCode:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the object with the specified range of prices.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(firstPrice: NSDecimalNumber, secondPrice: NSDecimalNumber, currencyCode: String)
```

```objc
- (instancetype) initWithRangeBetweenPrice:(NSDecimalNumber *) firstPrice andPrice:(NSDecimalNumber *) secondPrice currencyCode:(NSString *) currencyCode;
```

#### Return Value

An initialized price range object or `nil` if the object could not be created.

#### Discussion

This method assigns the lesser of the two price values to the [`minimumPrice`](./minimumprice.md) property, and it assigns the greater of the two values to the [`maximumPrice`](./maximumprice.md) property.

## Parameters

- `firstPrice`: The first price. This parameter must not be `nil`.
- `secondPrice`: The second price. This parameter must not be `nil`.
- `currencyCode`: The ISO 4217 currency code to apply to the price information. You can get a list of possible currency codes using the [`isoCurrencyCodes`](../../Foundation/nslocale/isocurrencycodes.md) method of [`NSLocale`](../../Foundation/nslocale.md). For example, the string “USD” corresponds to United States dollars.

## See Also

### Creating a Price Range Object
- [convenience init(price: NSDecimalNumber, currencyCode: String)](./init%28price,currencycode%29.md)
  Initializes the object with the specified price information.
- [init(maximumPrice: NSDecimalNumber, currencyCode: String)](./init%28maximumprice,currencycode%29.md)
  Initializes the object with the specified maximum price information.
- [init(minimumPrice: NSDecimalNumber, currencyCode: String)](./init%28minimumprice,currencycode%29.md)
  Initializes the object with the specified minimum price information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpricerange/init(firstprice:secondprice:currencycode:))*