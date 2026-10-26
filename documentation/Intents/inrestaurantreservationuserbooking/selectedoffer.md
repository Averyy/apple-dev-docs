# selectedOffer

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The offer selected by the user.

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

#### Discussion

If the user selects a special offer when making the reservation, use this property to store the selected offer. You can retrieve the selected offer from the [`selectedOffer`](../inbookrestaurantreservationintent/selectedoffer.md) property of the [`INBookRestaurantReservationIntent`](../inbookrestaurantreservationintent.md) object when providing your response to that intent.

## See Also

### Accessing Special Offers
- [var advisementText: String?](./advisementtext.md)
  A user-readable string containing policies and information related to the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbooking/selectedoffer)*