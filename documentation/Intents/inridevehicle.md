# INRideVehicle

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A specific vehicle used by a ride-booking service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class INRideVehicle
```

```objc
@interface INRideVehicle : NSObject
```

## Mentions

- [Providing Live Status Updates](../SiriKit/providing-live-status-updates.md)

#### Overview

An [`INRideVehicle`](./inridevehicle.md) object provides information about a vehicle in your fleet. Use a vehicle object to convey details about a specific vehicle to the user. Siri and Maps present information about your vehicle’s location on the map and let the user know when the vehicle arrives.

You create an [`INRideVehicle`](./inridevehicle.md) object when the user books a ride or when you provide the current status of a ride. You assign the vehicle object to the [`vehicle`](./inridestatus/vehicle.md) property of the [`INRideStatus`](./inridestatus.md) object that you include with your response.

## Topics

### Specifying the Vehicle’s Location
- [var location: CLLocation?](./inridevehicle/location.md)
  The most recent location of the vehicle.
- [var mapAnnotationImage: INImage?](./inridevehicle/mapannotationimage.md)
  The image to use for the vehicle when displaying its position on the map.
### Specifying the Vehicle Description
- [var registrationPlate: String?](./inridevehicle/registrationplate.md)
  The text on the license plate or registration plate of the vehicle.
- [var manufacturer: String?](./inridevehicle/manufacturer.md)
  The name of the vehicle’s manufacturer.
- [var model: String?](./inridevehicle/model.md)
  The model of the vehicle.
### Initializers
- [init?(coder: NSCoder)](./inridevehicle/init%28coder%29.md)

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
- [class INRideFareLineItem](./inridefarelineitem.md)
  A specific type of ride-related charge.
- [class INRidePartySizeOption](./inridepartysizeoption.md)
  The price of a ride involving the specified number of people.
- [class INRideCompletionStatus](./inridecompletionstatus.md)
  Additional details about whether a ride completed successfully or someone canceled the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridevehicle)*