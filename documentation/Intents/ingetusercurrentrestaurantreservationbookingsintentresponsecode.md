# INGetUserCurrentRestaurantReservationBookingsIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

## Declaration

```swift
enum INGetUserCurrentRestaurantReservationBookingsIntentResponseCode
```

```c
enum INGetUserCurrentRestaurantReservationBookingsIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.success](./ingetusercurrentrestaurantreservationbookingsintentresponsecode/success.md)
  You successfully handled the intent.
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.failure](./ingetusercurrentrestaurantreservationbookingsintentresponsecode/failure.md)
  You were unable to fetch the user’s reservations.
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.failureRequestUnsatisfiable](./ingetusercurrentrestaurantreservationbookingsintentresponsecode/failurerequestunsatisfiable.md)
  The intent object contained conflicting information.
- [INGetUserCurrentRestaurantReservationBookingsIntentResponseCode.unspecified](./ingetusercurrentrestaurantreservationbookingsintentresponsecode/unspecified.md)
  The request did not contain enough information for you to proceed.
### Initializers
- [init?(rawValue: Int)](./ingetusercurrentrestaurantreservationbookingsintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INGetUserCurrentRestaurantReservationBookingsIntentResponseCode](./ingetusercurrentrestaurantreservationbookingsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintentresponsecode)*