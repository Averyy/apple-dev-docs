# initWithPickupLocation:dropOffLocation:rideOptionName:partySize:paymentMethod:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes an intent object with the specified ride information.

**Availability**:
- iOS 10.0+ - Deprecated in 10.3
- iPadOS 10.0+ - Deprecated in 10.3
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 10.2
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.2

> **Deprecated**: Use [`initWithPickupLocation:dropOffLocation:rideOptionName:partySize:paymentMethod:scheduledPickupTime:`](./initwithpickuplocation_dropofflocation_rideoptionname_partysize_paymentmethod_scheduledpickuptime_.md) instead.

## Declaration

```objc
- (instancetype) initWithPickupLocation:(CLPlacemark *) pickupLocation dropOffLocation:(CLPlacemark *) dropOffLocation rideOptionName:(INSpeakableString *) rideOptionName partySize:(NSNumber *) partySize paymentMethod:(INPaymentMethod *) paymentMethod;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user tries to book a ride. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `pickupLocation`: The starting location for the ride.
- `dropOffLocation`: The destination of the ride.
- `rideOptionName`: The name of the ride option (if any) selected by the user.
- `partySize`: The number of passengers that the ride must accommodate.
- `paymentMethod`: The payment method requested by the user.

## See Also

### Initializing the Intent Object
- [- initWithPickupLocation:dropOffLocation:rideOptionName:partySize:paymentMethod:scheduledPickupTime:](./initwithpickuplocation_dropofflocation_rideoptionname_partysize_paymentmethod_scheduledpickuptime_.md)
  Initializes an intent object with the specified ride information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintent/initwithpickuplocation:dropofflocation:rideoptionname:partysize:paymentmethod:)*