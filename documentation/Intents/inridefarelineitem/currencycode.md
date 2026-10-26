# currencyCode

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The ISO 4217 currency code that applies to the price information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var currencyCode: String! { get }
```

```objc
@property (nonatomic, readonly) NSString * currencyCode;
```

#### Discussion

Use this value to determine the appropriate currency designator to apply to the value in the [`price`](./price.md) property. To retrieve the list of available currency codes, call the [`isoCurrencyCodes`](../../Foundation/nslocale/isocurrencycodes.md) method of the [`NSLocale`](../../Foundation/nslocale.md) class.

## See Also

### Getting the Line Item Information
- [var title: String!](./title.md)
  The localized string containing a description of the charge.
- [var price: NSDecimalNumber!](./price.md)
  The cost value of the line item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridefarelineitem/currencycode)*