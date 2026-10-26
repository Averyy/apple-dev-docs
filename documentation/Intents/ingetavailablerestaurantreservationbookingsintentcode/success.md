# INGetAvailableRestaurantReservationBookingsIntentCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully handled the intent.

## Declaration

```swift
case success
```

```c
INGetAvailableRestaurantReservationBookingsIntentCodeSuccess
```

#### Discussion

Use this code when your app successfully returns one or more [`INRestaurantReservationBooking`](../inrestaurantreservationbooking.md) objects that fall within the request time boundaries.

## See Also

### Constants
- [INGetAvailableRestaurantReservationBookingsIntentCode.failure](./failure.md)
  You were unable to provide a list of possible reservation times.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnsatisfiable](./failurerequestunsatisfiable.md)
  You could not complete the request because the data you received from Maps was invalid.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnspecified](./failurerequestunspecified.md)
  There was a failure in getting the requested booking times and the cause of the failure is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentcode/success)*