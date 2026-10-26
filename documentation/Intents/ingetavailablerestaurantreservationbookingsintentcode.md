# INGetAvailableRestaurantReservationBookingsIntentCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

## Declaration

```swift
enum INGetAvailableRestaurantReservationBookingsIntentCode
```

```c
enum INGetAvailableRestaurantReservationBookingsIntentCode : NSInteger;
```

## Topics

### Constants
- [INGetAvailableRestaurantReservationBookingsIntentCode.success](./ingetavailablerestaurantreservationbookingsintentcode/success.md)
  You successfully handled the intent.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failure](./ingetavailablerestaurantreservationbookingsintentcode/failure.md)
  You were unable to provide a list of possible reservation times.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnsatisfiable](./ingetavailablerestaurantreservationbookingsintentcode/failurerequestunsatisfiable.md)
  You could not complete the request because the data you received from Maps was invalid.
- [INGetAvailableRestaurantReservationBookingsIntentCode.failureRequestUnspecified](./ingetavailablerestaurantreservationbookingsintentcode/failurerequestunspecified.md)
  There was a failure in getting the requested booking times and the cause of the failure is unknown.
### Initializers
- [init?(rawValue: Int)](./ingetavailablerestaurantreservationbookingsintentcode/init%28rawvalue%29.md)

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
- [var code: INGetAvailableRestaurantReservationBookingsIntentCode](./ingetavailablerestaurantreservationbookingsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentcode)*