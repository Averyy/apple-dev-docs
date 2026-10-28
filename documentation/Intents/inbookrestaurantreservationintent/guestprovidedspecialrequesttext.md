# guestProvidedSpecialRequestText

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Information about any special requests made by the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var guestProvidedSpecialRequestText: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * guestProvidedSpecialRequestText;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * guestProvidedSpecialRequestText;
```

## Discussion

This property inclues and special requests made during booking. For example, the user might of asked for a non-smoking table or included special dietary requests when making a reservation. You should forward any special requests to the restaurant.

## See Also

### Getting Special Requests and Offers
- [var selectedOffer: INRestaurantOffer?](./selectedoffer.md)
  The special offer, if any, selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintent/guestprovidedspecialrequesttext)*