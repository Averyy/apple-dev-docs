# INCurrencyAmount

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An amount of money to transfer during a financial transaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INCurrencyAmount
```

```objc
@interface INCurrencyAmount : NSObject
```

#### Overview

An [`INCurrencyAmount`](./incurrencyamount.md) object encapsulates a monetary value and the currency used to express that value. You use these objects to specify payment amounts when handling intents that involve the transfer of money.

## Topics

### Initializing a Currency Amount Object
- [init(amount: NSDecimalNumber, currencyCode: String)](./incurrencyamount/init%28amount,currencycode%29.md)
  Initializes a currency amount object with the specified values.
### Getting the Currency Information
- [var amount: NSDecimalNumber?](./incurrencyamount/amount.md)
  The monetary amount associated with the currency.
- [var currencyCode: String?](./incurrencyamount/currencycode.md)
  The ISO 4217 currency code that applies to the monetary amount.
### Initializers
- [init?(coder: NSCoder)](./incurrencyamount/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Monetary
- [class INPriceRange](./inpricerange.md)
  Price information, as a range of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incurrencyamount)*