# init(restaurant:booking:partySize:bookingIdentifier:guest:selectedOffer:guestProvidedSpecialRequestText:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified booking information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(restaurant: INRestaurant, booking bookingDateComponents: DateComponents, partySize: Int, bookingIdentifier: String?, guest: INRestaurantGuest?, selectedOffer: INRestaurantOffer?, guestProvidedSpecialRequestText: String?)
```

```objc
- (instancetype) initWithRestaurant:(INRestaurant *) restaurant bookingDateComponents:(NSDateComponents *) bookingDateComponents partySize:(NSUInteger) partySize bookingIdentifier:(NSString *) bookingIdentifier guest:(INRestaurantGuest *) guest selectedOffer:(INRestaurantOffer *) selectedOffer guestProvidedSpecialRequestText:(NSString *) guestProvidedSpecialRequestText;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user asks to create a restaurant booking. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `restaurant`: The restaurant to contact regarding the booking.
- `bookingDateComponents`: The date and time of the reservation.
- `partySize`: The total number of people in the user’s party.
- `bookingIdentifier`: The unique identifier associated with the initial reservation data.
- `guest`: The identity of the guest associated to associate with the reservation.
- `selectedOffer`: The special offer, if any, selected by the user.
- `guestProvidedSpecialRequestText`: Information about any special requests made by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintent/init(restaurant:booking:partysize:bookingidentifier:guest:selectedoffer:guestprovidedspecialrequesttext:))*