# INBookRestaurantReservationIntentCode.denied

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The restaurant declined the reservation.

## Declaration

```swift
case denied
```

```c
INBookRestaurantReservationIntentCodeDenied
```

## Discussion

Use this code when the restaurant declines the reservation for any reason.

## See Also

### Constants
- [INBookRestaurantReservationIntentCode.success](./success.md)
  You successfully handled the intent.
- [INBookRestaurantReservationIntentCode.failure](./failure.md)
  You were unable to create the reservation object in your system.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to make the reservation.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchMustVerifyCredentials](./failurerequiringapplaunchmustverifycredentials.md)
  Your app failed to create the reservation because the user’s credentials were invalid or missing.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentcode/denied)*