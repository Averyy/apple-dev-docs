# init(personHandle:nameComponents:displayName:image:rating:phoneNumber:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes and returns a ride driver object using a set of name components and other driver information.

**Availability**:
- iOS 10.0+ - Deprecated in 10.2
- iPadOS 10.0+ - Deprecated in 10.2
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.1

> **Deprecated**: Use the designated initializer instead

## Declaration

```swift
convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, rating: String?, phoneNumber: String?)
```

```objc
- (instancetype) initWithPersonHandle:(INPersonHandle *) personHandle nameComponents:(NSPersonNameComponents *) nameComponents displayName:(NSString *) displayName image:(INImage *) image rating:(NSString *) rating phoneNumber:(NSString *) phoneNumber;
```

#### Return Value

An initialized driver object or `nil` if the object could not be created.

#### Discussion

You can’t change the driver information after initialization, so specify as much information as you have.

## Parameters

- `personHandle`: A handle to use when identifying the driver.
- `nameComponents`: The name of the driver, specified as a set of name components.
- `displayName`: The name of the driver in a user-readable format. This string is displayed to the user by Siri or Maps.
- `image`: A picture of the driver.
- `rating`: The driver’s rating. Strings should be short and informative. For example, you might specify the string “Good” or a string containing Unicode star (★, ☆) characters.
- `phoneNumber`: The driver’s phone number. The user should be able to contact the driver at this number to coordinate ride details.

## See Also

### Initializing a Ride Driver Object
- [init(phoneNumber: String, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, rating: String?)](./init%28phonenumber,namecomponents,displayname,image,rating%29.md)
  Initializes and returns a ride driver object using a set of name components and other driver information.
- [convenience init(handle: String, displayName: String?, image: INImage?, rating: String?, phoneNumber: String?)](./init%28handle,displayname,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a display name and other driver information.
- [convenience init(handle: String, nameComponents: PersonNameComponents, image: INImage?, rating: String?, phoneNumber: String?)](./init%28handle,namecomponents,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a set of name components and other driver information


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridedriver/init(personhandle:namecomponents:displayname:image:rating:phonenumber:))*