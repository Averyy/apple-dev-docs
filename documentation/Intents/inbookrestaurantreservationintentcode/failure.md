# INBookRestaurantReservationIntentCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to create the reservation object in your system.

## Declaration

```swift
case failure
```

```c
INBookRestaurantReservationIntentCodeFailure
```

#### Discussion

Use this code for both transient and unrecoverable errors that prevented you from creating the reservation.

## See Also

### Constants
- [INBookRestaurantReservationIntentCode.success](./success.md)
  You successfully handled the intent.
- [INBookRestaurantReservationIntentCode.denied](./denied.md)
  The restaurant declined the reservation.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to make the reservation.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchMustVerifyCredentials](./failurerequiringapplaunchmustverifycredentials.md)
  Your app failed to create the reservation because the user’s credentials were invalid or missing.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentcode/failure)*