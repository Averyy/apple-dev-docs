# userBooking

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The detailed information about the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var userBooking: INRestaurantReservationUserBooking? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INRestaurantReservationUserBooking * userBooking;
```

*macOS*

```objc
@property (atomic, copy, nullable) INRestaurantReservationUserBooking * userBooking;
```

#### Discussion

Use this property to specify the details of the user’s reservation. When creating the [`INRestaurantReservationUserBooking`](../inrestaurantreservationuserbooking.md) object, provide as much information as possible. The system conveys information from this object back to the user through the system’s reservation interfaces.

## See Also

### Accessing the Response Information
- [var code: INBookRestaurantReservationIntentCode](./code.md)
  The code indicating whether you successfully handled the intent.
- [enum INBookRestaurantReservationIntentCode](../inbookrestaurantreservationintentcode.md)
  Constants indicating the state of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentresponse/userbooking)*