# init(minimumPrice:currencyCode:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the object with the specified minimum price information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(minimumPrice: NSDecimalNumber, currencyCode: String)
```

```objc
- (instancetype) initWithMinimumPrice:(NSDecimalNumber *) minimumPrice currencyCode:(NSString *) currencyCode;
```

## Return Value

An initialized price range object or `nil` if the object could not be created.

## Discussion

This method does not assign a value to the [`maximumPrice`](./maximumprice.md) property.

## Parameters

- `minimumPrice`: The minimum price value. This value is assigned to the [`minimumPrice`](./minimumprice.md) property.
- `currencyCode`: The ISO 4217 currency code to apply to the price information. You can get a list of possible currency codes using the [`isoCurrencyCodes`](../../Foundation/nslocale/isocurrencycodes.md) method of [`NSLocale`](../../Foundation/nslocale.md). For example, the string “USD” corresponds to United States dollars.

## See Also

### Creating a Price Range Object
- [convenience init(price: NSDecimalNumber, currencyCode: String)](./init%28price,currencycode%29.md)
  Initializes the object with the specified price information.
- [init(firstPrice: NSDecimalNumber, secondPrice: NSDecimalNumber, currencyCode: String)](./init%28firstprice,secondprice,currencycode%29.md)
  Initializes the object with the specified range of prices.
- [init(maximumPrice: NSDecimalNumber, currencyCode: String)](./init%28maximumprice,currencycode%29.md)
  Initializes the object with the specified maximum price information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpricerange/init(minimumprice:currencycode:))*