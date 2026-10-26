# guest

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The identity of the person making the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var guest: INRestaurantGuest? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INRestaurantGuest * guest;
```

*macOS*

```objc
@property (atomic, copy, nullable) INRestaurantGuest * guest;
```

#### Discussion

Use this property to specify the identity of the person making the reservation. Depending on the preferences you specify in the [`guestDisplayPreferences`](./guestdisplaypreferences.md) property, this person may or may not be the person associated with any newly created reservations.

## See Also

### Specifying the Response Details
- [var guestDisplayPreferences: INRestaurantGuestDisplayPreferences?](./guestdisplaypreferences.md)
  The options for specifying how you want guest information conveyed to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetrestaurantguestintentresponse/guest)*