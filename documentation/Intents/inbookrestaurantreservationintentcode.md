# INBookRestaurantReservationIntentCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

## Declaration

```swift
enum INBookRestaurantReservationIntentCode
```

```c
enum INBookRestaurantReservationIntentCode : NSInteger;
```

## Topics

### Constants
- [INBookRestaurantReservationIntentCode.success](./inbookrestaurantreservationintentcode/success.md)
  You successfully handled the intent.
- [INBookRestaurantReservationIntentCode.denied](./inbookrestaurantreservationintentcode/denied.md)
  The restaurant declined the reservation.
- [INBookRestaurantReservationIntentCode.failure](./inbookrestaurantreservationintentcode/failure.md)
  You were unable to create the reservation object in your system.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunch](./inbookrestaurantreservationintentcode/failurerequiringapplaunch.md)
  The user must launch your app to make the reservation.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchMustVerifyCredentials](./inbookrestaurantreservationintentcode/failurerequiringapplaunchmustverifycredentials.md)
  Your app failed to create the reservation because the user’s credentials were invalid or missing.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./inbookrestaurantreservationintentcode/failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.
### Initializers
- [init?(rawValue: Int)](./inbookrestaurantreservationintentcode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing the Response Information
- [var code: INBookRestaurantReservationIntentCode](./inbookrestaurantreservationintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [var userBooking: INRestaurantReservationUserBooking?](./inbookrestaurantreservationintentresponse/userbooking.md)
  The detailed information about the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentcode)*