# INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnsatisfiable

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You could not complete the request because the data you received from Maps was invalid.

## Declaration

```swift
case failureRequestUnsatisfiable
```

```c
INGetAvailableRestaurantReservationBookingsIntentCodeFailureRequestUnsatisfiable
```

## Discussion

Use this code to indicate that you could not get the booking times with the provided data. Maps launches your app and passes it to the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object from your response so that you can try to get the information there.

## See Also

### Constants
- [INGetAvailableRestaurantReservationBookingsIntentCode.success](./success.md)
  You successfully handled the intent.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failure](./failure.md)
  You were unable to provide a list of possible reservation times.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnspecified](./failurerequestunspecified.md)
  There was a failure in getting the requested booking times and the cause of the failure is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentcode/failurerequestunsatisfiable)*