# init(handle:nameComponents:image:rating:phoneNumber:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes and returns a ride driver object using a set of name components and other driver information

**Availability**:
- iOS 10.0+ - Deprecated in 10.0
- iPadOS 10.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use the designated initializer instead

## Declaration

```swift
convenience init(handle: String, nameComponents: PersonNameComponents, image: INImage?, rating: String?, phoneNumber: String?)
```

```objc
- (instancetype) initWithHandle:(NSString *) handle nameComponents:(NSPersonNameComponents *) nameComponents image:(INImage *) image rating:(NSString *) rating phoneNumber:(NSString *) phoneNumber;
```

#### Return Value

An initialized driver object or `nil` if the object could not be created.

#### Discussion

You must specify all of the driver’s information at initialization time. You can’t change the values after initialization.

## Parameters

- `handle`: A string containing information that your app uses to identify the driver. You might use an email address, phone number, account name, or any information that lets you identify the user uniquely.
- `nameComponents`: The name of the driver, specified as a set of name components.
- `image`: A picture of the driver.
- `rating`: The driver’s rating. Strings should be short and informative. For example, you might specify the string “Good” or a string containing Unicode star (★, ☆) characters.
- `phoneNumber`: The driver’s phone number. The user should be able to contact the driver at this number to coordinate ride details.

## See Also

### Initializing a Ride Driver Object
- [init(phoneNumber: String, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, rating: String?)](./init%28phonenumber,namecomponents,displayname,image,rating%29.md)
  Initializes and returns a ride driver object using a set of name components and other driver information.
- [convenience init(handle: String, displayName: String?, image: INImage?, rating: String?, phoneNumber: String?)](./init%28handle,displayname,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a display name and other driver information.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, rating: String?, phoneNumber: String?)](./init%28personhandle,namecomponents,displayname,image,rating,phonenumber%29.md)
  Initializes and returns a ride driver object using a set of name components and other driver information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridedriver/init(handle:namecomponents:image:rating:phonenumber:))*