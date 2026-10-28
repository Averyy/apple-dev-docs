# INRideCompletionStatus

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Additional details about whether a ride completed successfully or someone canceled the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INRideCompletionStatus
```

```objc
@interface INRideCompletionStatus : NSObject
```

## Overview

An [`INRideCompletionStatus`](./inridecompletionstatus.md) object contains detailed information about the status of a completed ride. Use this object to provide details about whether the ride was successful or canceled. You can also provide details related to the cost of the ride and whether the rider made payment.

When updating the status of a ride, you provide a response object that contains an [`INRideStatus`](./inridestatus.md) object with details about the status. When the ride reaches the completed phase, create an instance of this class and assign it to the [`completionStatus`](./inridestatus/completionstatus.md) property of the ride status object.

## Topics

### Creating a Ride Completion Status Object
- [class func completed() -> Self](./inridecompletionstatus/completed%28%29.md)
  Creates an instance of this class that indicates the ride completed successfully.
- [class func completed(settled: INCurrencyAmount) -> Self](./inridecompletionstatus/completed%28settled%29.md)
  Creates an instance of this class that indicates the ride completed successfully and with the specified cost.
- [class func completed(outstanding: INCurrencyAmount) -> Self](./inridecompletionstatus/completed%28outstanding%29.md)
  Creates an instance of this class that indicates the ride completed successfully but still requires payment from the user.
- [class func completed(feedbackType: INRideFeedbackTypeOptions) -> Self](./inridecompletionstatus/completed%28feedbacktype%29.md)
  Creates an instance of this class that indicates the ride completed successfully but still requires feedback from the user.
- [class func canceledByService() -> Self](./inridecompletionstatus/canceledbyservice%28%29.md)
  Creates an instance of this class that indicates your service canceled the ride.
- [class func canceledByUser() -> Self](./inridecompletionstatus/canceledbyuser%28%29.md)
  Creates an instance of this class that indicates the user canceled the ride.
- [class func canceledMissedPickup() -> Self](./inridecompletionstatus/canceledmissedpickup%28%29.md)
  Creates an instance of this class that indicates someone canceled the ride because of a missed pickup.
### Providing a User Activity Object
- [var completionUserActivity: NSUserActivity?](./inridecompletionstatus/completionuseractivity.md)
  The user activity object indicating any additional steps the user needs to be take in your app.
### Getting the Status Information
- [var isCompleted: Bool](./inridecompletionstatus/iscompleted.md)
  A Boolean value indicating whether the ride completed successfully.
- [var isCanceled: Bool](./inridecompletionstatus/iscanceled.md)
  A Boolean value indicating whether someone canceled the ride for any reason.
- [var isMissedPickup: Bool](./inridecompletionstatus/ismissedpickup.md)
  A Boolean value indicating whether someone canceled the ride because the user was never picked up.
- [var isOutstanding: Bool](./inridecompletionstatus/isoutstanding.md)
  A Boolean indicating whether payment is still outstanding.
- [var paymentAmount: INCurrencyAmount?](./inridecompletionstatus/paymentamount.md)
  The amount paid or still outstanding for the ride.
### Requesting Feedback About the Ride
- [var feedbackType: INRideFeedbackTypeOptions](./inridecompletionstatus/feedbacktype.md)
  The type of feedback required for the ride before the user books a new ride can.
- [struct INRideFeedbackTypeOptions](./inridefeedbacktypeoptions.md)
  Constants indicating the type of feedback needed.
- [var defaultTippingOptions: Set<INCurrencyAmount>?](./inridecompletionstatus/defaulttippingoptions.md)
  An array of default tip amounts to display to the user.
### Initializers
- [init?(coder: NSCoder)](./inridecompletionstatus/init%28coder%29.md)

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
- [class INRidePartySizeOption](./inridepartysizeoption.md)
  The price of a ride involving the specified number of people.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus)*