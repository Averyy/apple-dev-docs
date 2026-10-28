# guestDisplayPreferences

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The options for specifying how you want guest information conveyed to the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var guestDisplayPreferences: INRestaurantGuestDisplayPreferences? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INRestaurantGuestDisplayPreferences * guestDisplayPreferences;
```

*macOS*

```objc
@property (atomic, copy, nullable) INRestaurantGuestDisplayPreferences * guestDisplayPreferences;
```

## Discussion

After returning your response, the system uses the preferences in this property to determine how to present guest information in the resulting system interface. Specifying a value for this property is your way of controlling how to display information about the user. For example, you might use this property to specify that you always want the user’s email address shown.

Maps uses the information in this property to configure the reservation interface it displays to users. If the value of this property is `nil`, Maps uses the default values associated with the properties of the [`INRestaurantGuestDisplayPreferences`](../inrestaurantguestdisplaypreferences.md) class.

## See Also

### Specifying the Response Details
- [var guest: INRestaurantGuest?](./guest.md)
  The identity of the person making the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetrestaurantguestintentresponse/guestdisplaypreferences)*