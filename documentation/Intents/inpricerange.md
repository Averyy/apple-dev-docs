# INPriceRange

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Price information, as a range of possible values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPriceRange
```

```objc
@interface INPriceRange : NSObject
```

## Overview

An [`INPriceRange`](./inpricerange.md) object encapsulates pricing information for a response that involves a charge for services. Price range objects can specify an exact price, a minimum price, a maximum price, or a specific price range.

You create price range objects when providing a response that includes pricing information. Use the price range objects to offer a quote on the cost of the services you are providing, to specify price tiers for services, or to specify more specific pricing information. The information you provide is displayed to the user in appropriate places.

## Topics

### Creating a Price Range Object
- [convenience init(price: NSDecimalNumber, currencyCode: String)](./inpricerange/init%28price,currencycode%29.md)
  Initializes the object with the specified price information.
- [init(firstPrice: NSDecimalNumber, secondPrice: NSDecimalNumber, currencyCode: String)](./inpricerange/init%28firstprice,secondprice,currencycode%29.md)
  Initializes the object with the specified range of prices.
- [init(maximumPrice: NSDecimalNumber, currencyCode: String)](./inpricerange/init%28maximumprice,currencycode%29.md)
  Initializes the object with the specified maximum price information.
- [init(minimumPrice: NSDecimalNumber, currencyCode: String)](./inpricerange/init%28minimumprice,currencycode%29.md)
  Initializes the object with the specified minimum price information.
### Getting the Price Range Information
- [var minimumPrice: NSDecimalNumber?](./inpricerange/minimumprice.md)
  The minimum price.
- [var maximumPrice: NSDecimalNumber?](./inpricerange/maximumprice.md)
  The maximum price.
- [var currencyCode: String](./inpricerange/currencycode.md)
  The ISO 4217 currency code that applies to the price information.
### Initializers
- [init?(coder: NSCoder)](./inpricerange/init%28coder%29.md)
- [init(rangeBetweenPrice: NSDecimalNumber, andPrice: NSDecimalNumber, currencyCode: String)](./inpricerange/init%28rangebetweenprice,andprice,currencycode%29.md)

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
- [class INCurrencyAmount](./incurrencyamount.md)
  An amount of money to transfer during a financial transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpricerange)*