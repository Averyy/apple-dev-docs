# CNContactVCardSerialization

**Framework**: Contacts  
**Kind**: class

An object you use to convert to and from a vCard representation of the user’s contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNContactVCardSerialization
```

## Topics

### Extracting Contacts from a vCard
- [class func contacts(with: Data) throws -> [CNContact]](cncontactvcardserialization/contacts(with:).md)
  Returns the contacts from the vCard data.
### Getting a vCard for Contacts
- [class func data(with: [CNContact]) throws -> Data](cncontactvcardserialization/data(with:).md)
  Returns the vCard representation of the specified contacts.
### Getting a Descriptor
- [class func descriptorForRequiredKeys() -> any CNKeyDescriptor](cncontactvcardserialization/descriptorforrequiredkeys.md)
  Use to fetch all contact keys required to create vCard data from a contact.

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
- [class CNContactsUserDefaults](cncontactsuserdefaults.md)
  An object that defines the default options to use when displaying contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactvcardserialization)*