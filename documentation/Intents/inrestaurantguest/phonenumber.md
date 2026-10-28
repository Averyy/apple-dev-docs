# phoneNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The phone number to use when contacting the user about reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var phoneNumber: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * phoneNumber;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * phoneNumber;
```

## Discussion

Make sure you format the string in this property in order to properly display it to the user. When actually booking the reservation, you can also pass the information to the restaurant that receives the booking, so that it has a way of contacting the user if they need to change the reservation later.

## See Also

### Accessing the Guest Information
- [var emailAddress: String?](./emailaddress.md)
  The email address to use when contacting the user about reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguest/phonenumber)*