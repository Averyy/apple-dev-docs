# initWithPickupLocation:dropOffLocation:rideOptionName:partySize:paymentMethod:scheduledPickupTime:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes an intent object with the specified ride information.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```objc
- (instancetype) initWithPickupLocation:(CLPlacemark *) pickupLocation dropOffLocation:(CLPlacemark *) dropOffLocation rideOptionName:(INSpeakableString *) rideOptionName partySize:(NSNumber *) partySize paymentMethod:(INPaymentMethod *) paymentMethod scheduledPickupTime:(INDateComponentsRange *) scheduledPickupTime;
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

## See Also

### Initializing the Intent Object
- [- initWithPickupLocation:dropOffLocation:rideOptionName:partySize:paymentMethod:](./initwithpickuplocation_dropofflocation_rideoptionname_partysize_paymentmethod_.md)
  Initializes an intent object with the specified ride information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintent/initwithpickuplocation:dropofflocation:rideoptionname:partysize:paymentmethod:scheduledpickuptime:)*