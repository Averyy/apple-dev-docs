# INGetAvailableRestaurantReservationBookingsIntentCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to provide a list of possible reservation times.

## Declaration

```swift
case failure
```

```c
INGetAvailableRestaurantReservationBookingsIntentCodeFailure
```

#### Discussion

Use this code for both transient and unrecoverable errors that prevented you from generating the list of times.

## See Also

### Constants
- [INGetAvailableRestaurantReservationBookingsIntentCode.success](./success.md)
  You successfully handled the intent.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnsatisfiable](./failurerequestunsatisfiable.md)
  You could not complete the request because the data you received from Maps was invalid.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnspecified](./failurerequestunspecified.md)
  There was a failure in getting the requested booking times and the cause of the failure is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentcode/failure)*