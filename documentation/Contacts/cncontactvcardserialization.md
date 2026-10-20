# CNContactVCardSerialization

**Framework**: Contacts  
**Kind**: class  
**Role**: Class

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

```objc
@interface CNContactVCardSerialization : NSObject
```

## Topics

### Extracting Contacts from a vCard
- [class func contacts(with: Data) throws -> [CNContact]](./cncontactvcardserialization/contacts%28with%29.md)
  Returns the contacts from the vCard data.
### Getting a vCard for Contacts
- [class func data(with: [CNContact]) throws -> Data](./cncontactvcardserialization/data%28with%29.md)
  Returns the vCard representation of the specified contacts.
### Getting a Descriptor
- [class func descriptorForRequiredKeys() -> any CNKeyDescriptor](./cncontactvcardserialization/descriptorforrequiredkeys%28%29.md)
  Use to fetch all contact keys required to create vCard data from a contact.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Formatters
- [class CNContactFormatter](./cncontactformatter.md)
  An object that you use to format contact information before displaying it to the user.
- [class CNPostalAddressFormatter](./cnpostaladdressformatter.md)
  An object that you use to format a contact’s postal addresses.
- [class CNContactsUserDefaults](./cncontactsuserdefaults.md)
  An object that defines the default options to use when displaying contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactvcardserialization)*