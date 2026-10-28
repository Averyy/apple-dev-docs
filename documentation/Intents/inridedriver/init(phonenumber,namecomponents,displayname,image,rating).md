# init(phoneNumber:nameComponents:displayName:image:rating:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes and returns a ride driver object using a set of name components and other driver information.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(phoneNumber: String, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, rating: String?)
```

```objc
- (instancetype) initWithPhoneNumber:(NSString *) phoneNumber nameComponents:(NSPersonNameComponents *) nameComponents displayName:(NSString *) displayName image:(INImage *) image rating:(NSString *) rating;
```

## Return Value

An initialized driver object or `nil` if the object could not be created.

## Discussion

You can’t change the driver information after initialization, so specify as much information as you have.

## Parameters

- `phoneNumber`: The driver’s phone number. The user should be able to contact the driver at this number to coordinate ride details.
- `nameComponents`: The name of the driver, specified as a set of name components.
- `displayName`: The name of the driver in a user-readable format. This string is displayed to the user by Siri or Maps.
- `image`: A picture of the driver.
- `rating`: The driver’s rating. Strings should be short and informative. For example, you might specify the string “Good” or a string containing Unicode star (★, ☆) characters.

## See Also

### Initializing a Ride Driver Object
- [convenience init(handle: String, displayName: String?, image: INImage?, rating: String?, phoneNumber: String?)](./init%28handle,displayname,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a display name and other driver information.
- [convenience init(handle: String, nameComponents: PersonNameComponents, image: INImage?, rating: String?, phoneNumber: String?)](./init%28handle,namecomponents,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a set of name components and other driver information
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, rating: String?, phoneNumber: String?)](./init%28personhandle,namecomponents,displayname,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a set of name components and other driver information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridedriver/init(phonenumber:namecomponents:displayname:image:rating:))*