# INRideStatus

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The status of a ride booked through a ride-booking service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class INRideStatus
```

```objc
@interface INRideStatus : NSObject
```

## Mentions

- [Providing Live Status Updates](../SiriKit/providing-live-status-updates.md)
- [Handling an Intent](../SiriKit/handling-an-intent.md)

## Overview

When the user books a ride or requests the status of a ride, you create an [`INRideStatus`](./inridestatus.md) object as part of your response and fill it with the relevant information. A ride status object conveys information about the current status of a ride, such as whether the ride is ongoing, completed, or has yet to occur. This object also contains details about the ride such as the pickup location, drop-off location, and information about the driver and vehicle. Siri and Maps display the information in this object to the user at appropriate times.

When configuring ride status objects, always provide values for as many properties as possible. Siri and Maps display almost all of the information that you provide to the user, so it is good to offer as many details as you can.

## Topics

### Accessing the Ride Identifier
- [var rideIdentifier: String?](./inridestatus/rideidentifier.md)
  The unique string that you use to identify the ride.
### Specifying the Ride Status
- [var phase: INRidePhase](./inridestatus/phase.md)
  The current status of the ride.
- [enum INRidePhase](./inridephase.md)
  Constants indicating the current ride status.
- [var completionStatus: INRideCompletionStatus?](./inridestatus/completionstatus.md)
  Information about how the ride ended.
### Accessing Ride Information
- [var vehicle: INRideVehicle?](./inridestatus/vehicle.md)
  The vehicle assigned to pick up the user.
- [var driver: INRideDriver?](./inridestatus/driver.md)
  The driver providing the ride.
- [var rideOption: INRideOption?](./inridestatus/rideoption.md)
  Information about the type of ride that you are offering to the user.
### Accessing the Pickup and Drop Off Times
- [var scheduledPickupTime: INDateComponentsRange?](./inridestatus/scheduledpickuptime.md)
  The scheduled pickup time for the user.
- [var estimatedPickupDate: Date?](./inridestatus/estimatedpickupdate.md)
  The estimated pickup time for the ride.
- [var estimatedPickupEndDate: Date?](./inridestatus/estimatedpickupenddate.md)
  The date after which the driver may stop waiting for the user.
- [var estimatedDropOffDate: Date?](./inridestatus/estimateddropoffdate.md)
  The estimated drop-off time for the ride.
### Accessing the Route Information
- [var pickupLocation: CLPlacemark?](./inridestatus/pickuplocation.md)
  The starting location for the ride.
- [var waypoints: [CLPlacemark]?](./inridestatus/waypoints.md)
  The intermediate waypoints for the journey.
- [var dropOffLocation: CLPlacemark?](./inridestatus/dropofflocation.md)
  The destination of the user.
### Providing User Activity Objects
- [var userActivityForCancelingInApplication: NSUserActivity?](./inridestatus/useractivityforcancelinginapplication.md)
  A user activity object for canceling the ride request.
- [var additionalActionActivities: [NSUserActivity]?](./inridestatus/additionalactionactivities.md)
  Additional activities that the user may choose to perform while the ride request is active.
### Initializers
- [init?(coder: NSCoder)](./inridestatus/init%28coder%29.md)

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
- [class INRideDriver](./inridedriver.md)
  Identifying information about a driver of a ride service.
- [class INRideVehicle](./inridevehicle.md)
  A specific vehicle used by a ride-booking service.
- [class INRideFareLineItem](./inridefarelineitem.md)
  A specific type of ride-related charge.
- [class INRidePartySizeOption](./inridepartysizeoption.md)
  The price of a ride involving the specified number of people.
- [class INRideCompletionStatus](./inridecompletionstatus.md)
  Additional details about whether a ride completed successfully or someone canceled the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus)*