# init(pickupLocation:dropOffLocation:rideOptionName:partySize:paymentMethod:scheduledPickupTime:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes an intent object with the specified ride information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- watchOS 3.2+

## Declaration

```swift
@nonobjc
convenience init(pickupLocation: CLPlacemark? = nil, dropOffLocation: CLPlacemark? = nil, rideOptionName: INSpeakableString? = nil, partySize: Int? = nil, paymentMethod: INPaymentMethod? = nil, scheduledPickupTime: INDateComponentsRange? = nil)
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user tries to book a ride. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `pickupLocation`: The starting location for the ride.
- `dropOffLocation`: The destination of the ride.
- `rideOptionName`: The name of the ride option (if any) selected by the user.
- `partySize`: The number of passengers that the ride must accommodate.
- `paymentMethod`: The payment method requested by the user.
- `scheduledPickupTime`: The time at which the user wants to be picked up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintent/init(pickuplocation:dropofflocation:rideoptionname:partysize:paymentmethod:scheduledpickuptime:))*