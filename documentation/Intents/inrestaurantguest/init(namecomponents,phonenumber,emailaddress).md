# init(nameComponents:phoneNumber:emailAddress:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the object with the specified name and contact information for the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(nameComponents: PersonNameComponents?, phoneNumber: String?, emailAddress: String?)
```

```objc
- (instancetype) initWithNameComponents:(NSPersonNameComponents *) nameComponents phoneNumber:(NSString *) phoneNumber emailAddress:(NSString *) emailAddress;
```

## Return Value

An initialized restaurant guest object or `nil` if the object could not be created.

## Discussion

This method stores a copy of the `phoneNumber` and `emailAddress` objects that you provide.

## Parameters

- `nameComponents`: The name of the user who is creating or managing the reservation.
- `phoneNumber`: The phone number to use when contacting the user about reservations. Specify the information as a user-readable string that can be displayed in the reservations interface.
- `emailAddress`: The email address to use when contacting the user about reservations. Specify the information as a user-readable string that can be displayed in the reservations interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguest/init(namecomponents:phonenumber:emailaddress:))*