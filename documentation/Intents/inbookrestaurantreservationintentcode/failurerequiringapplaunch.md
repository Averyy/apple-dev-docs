# INBookRestaurantReservationIntentCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to make the reservation.

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INBookRestaurantReservationIntentCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you cannot handle the request directly for a reason not covered by any other response code. Do not use it for general errors or to force the user to launch your app.

## See Also

### Constants
- [INBookRestaurantReservationIntentCode.success](./success.md)
  You successfully handled the intent.
- [INBookRestaurantReservationIntentCode.denied](./denied.md)
  The restaurant declined the reservation.
- [INBookRestaurantReservationIntentCode.failure](./failure.md)
  You were unable to create the reservation object in your system.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchMustVerifyCredentials](./failurerequiringapplaunchmustverifycredentials.md)
  Your app failed to create the reservation because the user’s credentials were invalid or missing.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentcode/failurerequiringapplaunch)*