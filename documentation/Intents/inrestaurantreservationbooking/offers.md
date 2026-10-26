# offers

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of special offers from the restaurant.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var offers: [INRestaurantOffer]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSArray<INRestaurantOffer *> * offers;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSArray<INRestaurantOffer *> * offers;
```

#### Discussion

If a given reservation has associated special offers, assign those offers to this property. The system presents the offers to the user, who then has the option of selecting one. Specify `nil` if there are no available offers. The default value of this property is `nil`.

## See Also

### Accessing the Reservation Information
- [var restaurant: INRestaurant](./restaurant.md)
  The restaurant associated with the reservation.
- [var partySize: Int](./partysize.md)
  The total number of guests in the party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking/offers)*