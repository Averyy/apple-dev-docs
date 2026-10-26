# INBookRestaurantReservationIntentCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully handled the intent.

## Declaration

```swift
case success
```

```c
INBookRestaurantReservationIntentCodeSuccess
```

#### Discussion

Use this code if your app successfully created the reservation object in your system. Use this code even if the restaurant itself has not yet confirmed the reservation. You can always update the status of the reservation later.

## See Also

### Constants
- [INBookRestaurantReservationIntentCode.denied](./denied.md)
  The restaurant declined the reservation.
- [INBookRestaurantReservationIntentCode.failure](./failure.md)
  You were unable to create the reservation object in your system.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to make the reservation.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchMustVerifyCredentials](./failurerequiringapplaunchmustverifycredentials.md)
  Your app failed to create the reservation because the user’s credentials were invalid or missing.
- [INBookRestaurantReservationIntentCode.failureRequiringAppLaunchServiceTemporarilyUnavailable](./failurerequiringapplaunchservicetemporarilyunavailable.md)
  Your service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentcode/success)*