# INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully handled the intent.

## Declaration

```swift
case success
```

```c
INGetUserCurrentRestaurantReservationBookingsIntentResponseCodeSuccess
```

#### Discussion

Use this code if your app was successful in fetching the user’s reservations, even if the fetch returned no results. Include all of the reservations that match the search criteria in the [`userCurrentBookings`](../ingetusercurrentrestaurantreservationbookingsintentresponse/usercurrentbookings.md) property of your response object.

## See Also

### Constants
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.failure](./failure.md)
  You were unable to fetch the user’s reservations.
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.failureRequestUnsatisfiable](./failurerequestunsatisfiable.md)
  The intent object contained conflicting information.
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.unspecified](./unspecified.md)
  The request did not contain enough information for you to proceed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintentresponsecode/success)*