# INRidePartySizeOption

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The price of a ride involving the specified number of people.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class INRidePartySizeOption
```

```objc
@interface INRidePartySizeOption : NSObject
```

## Mentions

- [Generating a List of Ride Options](../SiriKit/generating-a-list-of-ride-options.md)

## Overview

An [`INRidePartySizeOption`](./inridepartysizeoption.md) object describes many passengers and the special pricing that applies to a party of that size. When configuring a [`INRideOption`](./inrideoption.md) object, you create one or more instances of this class to specify pricing for the user’s party. Present this information to the user along with the other ride option information.

## Topics

### Initializing a Party Size Object
- [init(partySizeRange: NSRange, sizeDescription: String, priceRange: INPriceRange?)](./inridepartysizeoption/init%28partysizerange,sizedescription,pricerange%29.md)
  Initializes the object with the specified party size and price ranges.
### Getting the Party Size Information
- [var partySizeRange: NSRange](./inridepartysizeoption/partysizerange.md)
  The number of people in the party, specified as a minimum and maximum value.
- [var sizeDescription: String](./inridepartysizeoption/sizedescription.md)
  The user-visible description of the party size.
- [var priceRange: INPriceRange?](./inridepartysizeoption/pricerange.md)
  The pricing information for parties of the specified size.
### Initializers
- [init?(coder: NSCoder)](./inridepartysizeoption/init%28coder%29.md)

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
- [class INRideFareLineItem](./inridefarelineitem.md)
  A specific type of ride-related charge.
- [class INRideCompletionStatus](./inridecompletionstatus.md)
  Additional details about whether a ride completed successfully or someone canceled the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridepartysizeoption)*