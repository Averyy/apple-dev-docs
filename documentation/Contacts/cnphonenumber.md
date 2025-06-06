# CNPhoneNumber

**Framework**: Contacts  
**Kind**: class

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

#### Overview

`CNPhoneNumber` objects are thread-safe, and you may access their properties from any thread of your app.

## Topics

### Creating a Phone Number Object
- [init(stringValue: String)](cnphonenumber/init(stringvalue:).md)
  Returns a new phone number object initialized with the specified phone number string.
### Getting the Phone Number
- [var stringValue: String](cnphonenumber/stringvalue.md)
  The string value of the phone number.
### Getting Phone-Related Keys
- [let CNContactPhoneNumbersKey: String](cncontactphonenumberskey.md)
  A phone numbers of a contact.
### Deprecated
- [init!()](cnphonenumber/init.md)
- [class func new() -> Self!](cnphonenumber/new.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnphonenumber)*