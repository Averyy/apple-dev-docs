# INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.failureRequestUnsatisfiable

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The intent object contained conflicting information.

## Declaration

```swift
case failureRequestUnsatisfiable
```

```c
INGetUserCurrentRestaurantReservationBookingsIntentResponseCodeFailureRequestUnsatisfiable
```

## Discussion

Use this code if the intent object contained a specific reservation identifier and restaurant, but that the reservation’s restaurant did not match the specified restaurant.

## See Also

### Constants
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.failure](./failure.md)
  You were unable to fetch the user’s reservations.
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.unspecified](./unspecified.md)
  The request did not contain enough information for you to proceed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintentresponsecode/failurerequestunsatisfiable)*