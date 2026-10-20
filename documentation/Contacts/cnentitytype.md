# CNEntityType

**Framework**: Contacts  
**Kind**: enum  
**Role**: Enumeration

The entities the user can grant access to.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CNEntityType
```

```c
enum CNEntityType : NSInteger;
```

## Topics

### Entities
- [CNEntityType.contacts](./cnentitytype/contacts.md)
  The user’s contacts.
### Initializers
- [init?(rawValue: Int)](./cnentitytype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Requesting access to the user’s contacts
- [func requestAccess(for: CNEntityType, completionHandler: (Bool, (any Error)?) -> Void)](./cncontactstore/requestaccess%28for,completionhandler%29.md)
  Requests access to the user’s contacts.
- [class func authorizationStatus(for: CNEntityType) -> CNAuthorizationStatus](./cncontactstore/authorizationstatus%28for%29.md)
  Returns the current authorization status to access the contact data.
- [enum CNAuthorizationStatus](./cnauthorizationstatus.md)
  An authorization status the user can grant for an app to access the specified entity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnentitytype)*