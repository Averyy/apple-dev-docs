# CNContactType

**Framework**: Contacts  
**Kind**: enum  
**Role**: Enumeration

The types a contact can be.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CNContactType
```

```c
enum CNContactType : NSInteger;
```

## Topics

### Constants
- [CNContactType.person](./cncontacttype/person.md)
  The contact is a person.
- [CNContactType.organization](./cncontacttype/organization.md)
  The contact is an Organization.
### Initializers
- [init?(rawValue: Int)](./cncontacttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Identifying the Contact
- [var identifier: String](./cncontact/identifier.md)
  A value that uniquely identifies a contact on the device.
- [var contactType: CNContactType](./cncontact/contacttype.md)
  An enum identifying the contact type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontacttype)*