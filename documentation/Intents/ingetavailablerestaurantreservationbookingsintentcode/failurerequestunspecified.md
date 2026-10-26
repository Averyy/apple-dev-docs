# INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnspecified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

There was a failure in getting the requested booking times and the cause of the failure is unknown.

## Declaration

```swift
case failureRequestUnspecified
```

```c
INGetAvailableRestaurantReservationBookingsIntentCodeFailureRequestUnspecified
```

#### Discussion

Maps launches your app and passes it to the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object from your response so that you can try to get the information there.

## See Also

### Constants
- [INGetAvailableRestaurantReservationBookingsIntentCode.success](./success.md)
  You successfully handled the intent.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failure](./failure.md)
  You were unable to provide a list of possible reservation times.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnsatisfiable](./failurerequestunsatisfiable.md)
  You could not complete the request because the data you received from Maps was invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentcode/failurerequestunspecified)*