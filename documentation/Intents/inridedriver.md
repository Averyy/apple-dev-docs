# INRideDriver

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Identifying information about a driver of a ride service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INRideDriver
```

```objc
@interface INRideDriver : INPerson
```

#### Overview

An [`INRideDriver`](./inridedriver.md) object encapsulates information about a driver associated with your ride service. This object stores basic information about the driver, including the driver’s name, picture, and phone number. You create an [`INRideDriver`](./inridedriver.md) object and assign it to the [`driver`](./inridestatus/driver.md) property of a [`INRideStatus`](./inridestatus.md) object when the user books a ride or when you update the status of an existing ride. SiriKit displays the driver information to the user at appropriate times.

This class is a subclass of [`INPerson`](./inperson.md) and contains properties that are relevant only for ride-booking services. For additional driver properties, see [`INPerson`](./inperson.md).

## Topics

### Initializing a Ride Driver Object
- [init(phoneNumber: String, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, rating: String?)](./inridedriver/init%28phonenumber,namecomponents,displayname,image,rating%29.md)
  Initializes and returns a ride driver object using a set of name components and other driver information.
- [convenience init(handle: String, displayName: String?, image: INImage?, rating: String?, phoneNumber: String?)](./inridedriver/init%28handle,displayname,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a display name and other driver information.
- [convenience init(handle: String, nameComponents: PersonNameComponents, image: INImage?, rating: String?, phoneNumber: String?)](./inridedriver/init%28handle,namecomponents,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a set of name components and other driver information
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, rating: String?, phoneNumber: String?)](./inridedriver/init%28personhandle,namecomponents,displayname,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a set of name components and other driver information.
### Getting the Driver Information
- [var rating: String?](./inridedriver/rating.md)
  The driver’s current rating.
- [var phoneNumber: String?](./inridedriver/phonenumber.md)
  The driver’s phone number.

## Relationships

### Inherits From
- [INPerson](./inperson.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INSpeakable](./inspeakable.md)
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
- [class INRideVehicle](./inridevehicle.md)
  A specific vehicle used by a ride-booking service.
- [class INRideFareLineItem](./inridefarelineitem.md)
  A specific type of ride-related charge.
- [class INRidePartySizeOption](./inridepartysizeoption.md)
  The price of a ride involving the specified number of people.
- [class INRideCompletionStatus](./inridecompletionstatus.md)
  Additional details about whether a ride completed successfully or someone canceled the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridedriver)*