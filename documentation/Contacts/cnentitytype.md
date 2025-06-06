# CNEntityType

**Framework**: Contacts  
**Kind**: enum

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

## Topics

### Entities
- [CNEntityType.contacts](cnentitytype/contacts.md)
  The user’s contacts.
### Initializers
- [init?(rawValue: Int)](cnentitytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func requestAccess(for: CNEntityType, completionHandler: (Bool, (any Error)?) -> Void)](cncontactstore/requestaccess(for:completionhandler:).md)
  Requests access to the user’s contacts.
- [class func authorizationStatus(for: CNEntityType) -> CNAuthorizationStatus](cncontactstore/authorizationstatus(for:).md)
  Returns the current authorization status to access the contact data.
- [enum CNAuthorizationStatus](cnauthorizationstatus.md)
  An authorization status the user can grant for an app to access the specified entity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnentitytype)*