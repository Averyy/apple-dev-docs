# selectedOffer

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The special offer, if any, selected by the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var selectedOffer: INRestaurantOffer? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INRestaurantOffer * selectedOffer;
```

*macOS*

```objc
@property (atomic, copy, nullable) INRestaurantOffer * selectedOffer;
```

## Discussion

If the reservation option selected by the user contained any special offers, this property contains the offer that the user selected. Prior to booking, you create [`INRestaurantReservationBooking`](../inrestaurantreservationbooking.md) objects with the details of the reservation options, including any special offers available at that time. If the user selects one of the options, the system puts the information about the selected offer in this property. You should convey the offer data to the restaurant along with the other details of the user’s reservation.

## See Also

### Getting Special Requests and Offers
- [var guestProvidedSpecialRequestText: String?](./guestprovidedspecialrequesttext.md)
  Information about any special requests made by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintent/selectedoffer)*