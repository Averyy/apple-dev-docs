# requiresManualRequest

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the reservation requires manually contacting the restaurant to confirm the details.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var requiresManualRequest: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) BOOL requiresManualRequest;
```

*macOS*

```objc
@property (atomic) BOOL requiresManualRequest;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md), which indicates that your service can place reservations with the restaurant electronically. Change the value to [`true`](../../Swift/true.md) if your service must manually contact the restaurant in order to make the reservation.

## See Also

### Configuring the Required Information
- [var requiresName: Bool](./requiresname.md)
  A Boolean indicating whether the reservation requires a guest name before booking.
- [var requiresEmailAddress: Bool](./requiresemailaddress.md)
  A Boolean indicating whether the reservation requires an email address before it booking.
- [var requiresPhoneNumber: Bool](./requiresphonenumber.md)
  A Boolean indicating whether the reservation requires a phone number before booking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking/requiresmanualrequest)*