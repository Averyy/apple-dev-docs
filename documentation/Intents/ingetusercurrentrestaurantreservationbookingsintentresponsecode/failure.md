# INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to fetch the user’s reservations.

## Declaration

```swift
case failure
```

```c
INGetUserCurrentRestaurantReservationBookingsIntentResponseCodeFailure
```

#### Discussion

Use this code for both transient and unrecoverable errors that prevented you from performing the fetch operation.

## See Also

### Constants
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.failureRequestUnsatisfiable](./failurerequestunsatisfiable.md)
  The intent object contained conflicting information.
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.unspecified](./unspecified.md)
  The request did not contain enough information for you to proceed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintentresponsecode/failure)*