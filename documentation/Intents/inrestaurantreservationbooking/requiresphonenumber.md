# requiresPhoneNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the reservation requires a phone number before booking.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var requiresPhoneNumber: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) BOOL requiresPhoneNumber;
```

*macOS*

```objc
@property (atomic) BOOL requiresPhoneNumber;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md). Change the value to [`true`](../../Swift/true.md) if the restaurant (or your service) requires a phone number to confirm the reservation.

## See Also

### Configuring the Required Information
- [var requiresName: Bool](./requiresname.md)
  A Boolean indicating whether the reservation requires a guest name before booking.
- [var requiresEmailAddress: Bool](./requiresemailaddress.md)
  A Boolean indicating whether the reservation requires an email address before it booking.
- [var requiresManualRequest: Bool](./requiresmanualrequest.md)
  A Boolean indicating whether the reservation requires manually contacting the restaurant to confirm the details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking/requiresphonenumber)*