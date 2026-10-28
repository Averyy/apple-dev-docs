# INRideFareLineItem

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A specific type of ride-related charge.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class INRideFareLineItem
```

```objc
@interface INRideFareLineItem : NSObject
```

## Overview

Create one or more [`INRideFareLineItem`](./inridefarelineitem.md) objects when you need to break down the cost of a ride using different pricing rules. For example, one line item might specify the base charge of the ride and a second line item might specify the per-mile charge. When displaying the ride information to the user, Siri and Maps display the line-item information.

The inclusion of line items in an [`INRideOption`](./inrideoption.md) object is optional but recommended when the cost of the ride involves separate charges. When appropriate, create one or more [`INRideFareLineItem`](./inridefarelineitem.md) objects and attach them to your ride option object. Siri and Maps use the currency code you specify to apply the appropriate currency designator to the price information.

## Topics

### Initializing a Ride Fare Object
- [init!(title: String!, price: NSDecimalNumber!, currencyCode: String!)](./inridefarelineitem/init%28title,price,currencycode%29.md)
  Initializes the line item object with the specified title and pricing information.
### Getting the Line Item Information
- [var title: String!](./inridefarelineitem/title.md)
  The localized string containing a description of the charge.
- [var price: NSDecimalNumber!](./inridefarelineitem/price.md)
  The cost value of the line item.
- [var currencyCode: String!](./inridefarelineitem/currencycode.md)
  The ISO 4217 currency code that applies to the price information.
### Initializers
- [init?(coder: NSCoder)](./inridefarelineitem/init%28coder%29.md)

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

### Data Objects
- [class INRideOption](./inrideoption.md)
  Details about a type of ride offered by your ride-booking service.
- [class INRideStatus](./inridestatus.md)
  The status of a ride booked through a ride-booking service.
- [class INRideDriver](./inridedriver.md)
  Identifying information about a driver of a ride service.
- [class INRideVehicle](./inridevehicle.md)
  A specific vehicle used by a ride-booking service.
- [class INRidePartySizeOption](./inridepartysizeoption.md)
  The price of a ride involving the specified number of people.
- [class INRideCompletionStatus](./inridecompletionstatus.md)
  Additional details about whether a ride completed successfully or someone canceled the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridefarelineitem)*