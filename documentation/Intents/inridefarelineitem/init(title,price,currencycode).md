# init(title:price:currencyCode:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the line item object with the specified title and pricing information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init!(title: String!, price: NSDecimalNumber!, currencyCode: String!)
```

```objc
- (instancetype) initWithTitle:(NSString *) title price:(NSDecimalNumber *) price currencyCode:(NSString *) currencyCode;
```

## Return Value

An initialized line item object or `nil` if the object could not be created.

## Parameters

- `title`: A localized string that describes the meaning of the charge. For example, you might specify the strings “Base fare”, “Per-mile charge”, or “+ per-mile”.
- `price`: The price for the line item.
- `currencyCode`: The ISO 4217 currency code to apply to the line item’s price. You can get a list of possible currency codes using the [`isoCurrencyCodes`](../../Foundation/nslocale/isocurrencycodes.md) method of [`NSLocale`](../../Foundation/nslocale.md). For example, the string “USD” corresponds to United States dollars. This code used to determine the currency designator to apply to the `price` information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridefarelineitem/init(title:price:currencycode:))*