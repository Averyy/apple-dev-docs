# CNAuthorizationStatus

**Framework**: Contacts  
**Kind**: enum  
**Role**: Enumeration

An authorization status the user can grant for an app to access the specified entity type.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CNAuthorizationStatus
```

```c
enum CNAuthorizationStatus : NSInteger;
```

## Topics

### Authorization statuses
- [CNAuthorizationStatus.notDetermined](./cnauthorizationstatus/notdetermined.md)
  The user has not yet made a choice regarding whether the application may access contact data.
- [CNAuthorizationStatus.restricted](./cnauthorizationstatus/restricted.md)
  The application is not authorized to access contact data. The user cannot change this application’s status, possibly due to active restrictions such as parental controls being in place.
- [CNAuthorizationStatus.denied](./cnauthorizationstatus/denied.md)
  The user explicitly denied access to contact data for the application.
- [CNAuthorizationStatus.authorized](./cnauthorizationstatus/authorized.md)
  The application is authorized to access contact data.
- [CNAuthorizationStatus.limited](./cnauthorizationstatus/limited.md)
  The app has access to a limited subset of contacts, chosen by the person using the app.
### Initializers
- [init?(rawValue: Int)](./cnauthorizationstatus/init%28rawvalue%29.md)

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
- [enum CNEntityType](./cnentitytype.md)
  The entities the user can grant access to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnauthorizationstatus)*