# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether you successfully handled the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var code: INBookRestaurantReservationIntentCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INBookRestaurantReservationIntentCode code;
```

*macOS*

```objc
@property (atomic, readonly) INBookRestaurantReservationIntentCode code;
```

## Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

## See Also

### Accessing the Response Information
- [enum INBookRestaurantReservationIntentCode](../inbookrestaurantreservationintentcode.md)
  Constants indicating the state of the response.
- [var userBooking: INRestaurantReservationUserBooking?](./userbooking.md)
  The detailed information about the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentresponse/code)*