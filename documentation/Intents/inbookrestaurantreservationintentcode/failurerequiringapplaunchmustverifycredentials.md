# INBookRestaurantReservationIntentCode.failureRequiringAppLaunchMustVerifyCredentials

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Your app failed to create the reservation because the user’s credentials were invalid or missing.

## Declaration

```swift
case failureRequiringAppLaunchMustVerifyCredentials
```

```c
INBookRestaurantReservationIntentCodeFailureRequiringAppLaunchMustVerifyCredentials
```

## Discussion

Use this code when you do not have valid credentials for the user. Maps launches your app and passes it to the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object from your response so that you can try to verify the user’s credentials there.

## See Also

### Constants
- [INBookRestaurantReservationIntentCode.success](./success.md)
  You successfully handled the intent.
- [INBookRestaurantReservationIntentCode.denied](./denied.md)
  The restaurant declined the reservation.
- [INBookRestaurantReservationIntentCode.failure](./failure.md)
  You were unable to create the reservation object in your system.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to make the reservation.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentcode/failurerequiringapplaunchmustverifycredentials)*