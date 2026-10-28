# INBookRestaurantReservationIntentCode.failureRequiringAppLaunchServiceTemporarilyUnavailable

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Your service is temporarily unavailable.

## Declaration

```swift
case failureRequiringAppLaunchServiceTemporarilyUnavailable
```

```c
INBookRestaurantReservationIntentCodeFailureRequiringAppLaunchServiceTemporarilyUnavailable
```

## Discussion

Use this code when your Intents extension is unable to contact your service and save the reservation data. Maps launches your app and passes it to the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object from your response so that you can try to complete the booking there.

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
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchMustVerifyCredentials](./failurerequiringapplaunchmustverifycredentials.md)
  Your app failed to create the reservation because the user’s credentials were invalid or missing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentcode/failurerequiringapplaunchservicetemporarilyunavailable)*