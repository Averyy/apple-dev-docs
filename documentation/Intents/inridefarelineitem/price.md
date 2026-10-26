# price

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The cost value of the line item.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var price: NSDecimalNumber! { get }
```

```objc
@property (nonatomic, readonly) NSDecimalNumber * price;
```

#### Discussion

This value in the [`currencyCode`](./currencycode.md) property determines the currency designator applied to this number. Siri and Maps display the line item’s title separately from the price information.

## See Also

### Getting the Line Item Information
- [var title: String!](./title.md)
  The localized string containing a description of the charge.
- [var currencyCode: String!](./currencycode.md)
  The ISO 4217 currency code that applies to the price information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridefarelineitem/price)*