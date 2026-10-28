# phoneNumberEditable

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the phone number field is editable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var phoneNumberEditable: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) BOOL phoneNumberEditable;
```

*macOS*

```objc
@property (atomic) BOOL phoneNumberEditable;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md), which lets the current user change the phone number assigned to a pending reservation.

## See Also

### Making the Guest Information Editable
- [var nameEditable: Bool](./nameeditable.md)
  A Boolean value indicating whether the name fields are editable.
- [var emailAddressEditable: Bool](./emailaddresseditable.md)
  A Boolean value indicating whether the email address field is editable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestdisplaypreferences/phonenumbereditable)*