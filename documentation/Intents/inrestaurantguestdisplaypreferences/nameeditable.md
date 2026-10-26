# nameEditable

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the name fields are editable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var nameEditable: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) BOOL nameEditable;
```

*macOS*

```objc
@property (atomic) BOOL nameEditable;
```

#### Discussion

The default value of this property is [`true`](../../Swift/true.md), which lets the current user change the name of the person assigned to the reservation. You might change this property to [`false`](../../Swift/false.md) if you require that reservations must be by the person who made them.

## See Also

### Making the Guest Information Editable
- [var emailAddressEditable: Bool](./emailaddresseditable.md)
  A Boolean value indicating whether the email address field is editable.
- [var phoneNumberEditable: Bool](./phonenumbereditable.md)
  A Boolean value indicating whether the phone number field is editable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestdisplaypreferences/nameeditable)*