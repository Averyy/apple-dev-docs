# title

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The localized string containing a description of the charge.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var title: String! { get }
```

```objc
@property (nonatomic, readonly) NSString * title;
```

## Discussion

This property contains a user-readable string describing the purpose of the charge. For example, it might contain the string “Base fare” or “Per-mile charge”. Siri and Maps display this information separately from the price information.

## See Also

### Getting the Line Item Information
- [var price: NSDecimalNumber!](./price.md)
  The cost value of the line item.
- [var currencyCode: String!](./currencycode.md)
  The ISO 4217 currency code that applies to the price information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridefarelineitem/title)*