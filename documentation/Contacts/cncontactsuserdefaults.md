# CNContactsUserDefaults

**Framework**: Contacts  
**Kind**: class

An object that defines the default options to use when displaying contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNContactsUserDefaults
```

## Topics

### Getting the Shared Database
- [class func shared() -> Self](cncontactsuserdefaults/shared.md)
  The singleton contacts user defaults object.
### Getting the Default Values
- [var countryCode: String](cncontactsuserdefaults/countrycode.md)
  An ISO country code.
- [var sortOrder: CNContactSortOrder](cncontactsuserdefaults/sortorder.md)
  Default sorting order by name.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CNContactFormatter](cncontactformatter.md)
  An object that you use to format contact information before displaying it to the user.
- [class CNPostalAddressFormatter](cnpostaladdressformatter.md)
  An object that you use to format a contact’s postal addresses.
- [class CNContactVCardSerialization](cncontactvcardserialization.md)
  An object you use to convert to and from a vCard representation of the user’s contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactsuserdefaults)*