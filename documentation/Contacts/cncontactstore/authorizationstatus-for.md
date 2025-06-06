# authorizationStatus(for:)

**Framework**: Contacts  
**Kind**: method

Returns the current authorization status to access the contact data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func authorizationStatus(for entityType: CNEntityType) -> CNAuthorizationStatus
```

## Mentions

- [Accessing the contact store](accessing-the-contact-store.md)

#### Return Value

The current authorization status to access the contact data.

#### Discussion

Based on the authorization status, your application might display or hide its UI elements that access any Contacts API. This method is thread-safe and will not block your application. To see different authorization status, see `CNAuthorizationStatus`.

## Parameters

- `entityType`: Set to  .

## See Also

- [func requestAccess(for: CNEntityType, completionHandler: (Bool, (any Error)?) -> Void)](cncontactstore/requestaccess(for:completionhandler:).md)
  Requests access to the user’s contacts.
- [enum CNAuthorizationStatus](cnauthorizationstatus.md)
  An authorization status the user can grant for an app to access the specified entity type.
- [enum CNEntityType](cnentitytype.md)
  The entities the user can grant access to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/authorizationstatus(for:))*