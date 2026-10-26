# CNPhoneNumber

**Framework**: Contacts  
**Kind**: class  
**Role**: Class

An immutable object representing a phone number for a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNPhoneNumber
```

```objc
@interface CNPhoneNumber : NSObject
```

#### Overview

`CNPhoneNumber` objects are thread-safe, and you may access their properties from any thread of your app.

## Topics

### Creating a Phone Number Object
- [init(stringValue: String)](./cnphonenumber/init%28stringvalue%29.md)
  Returns a new phone number object initialized with the specified phone number string.
- [+ phoneNumberWithStringValue:](./cnphonenumber/phonenumberwithstringvalue_.md)
  Returns a new phone number object initialized with the specified phone number string.
### Getting the Phone Number
- [var stringValue: String](./cnphonenumber/stringvalue.md)
  The string value of the phone number.
### Getting Phone-Related Keys
- [let CNContactPhoneNumbersKey: String](./cncontactphonenumberskey.md)
  A phone numbers of a contact.
### Deprecated
- [init!()](./cnphonenumber/init%28%29.md)
- [class func new() -> Self!](./cnphonenumber/new%28%29.md)
### Initializers
- [init?(coder: NSCoder)](./cnphonenumber/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnphonenumber)*