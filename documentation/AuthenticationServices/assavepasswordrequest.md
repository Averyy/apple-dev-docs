# ASSavePasswordRequest

**Framework**: Authentication Services  
**Kind**: class

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
class ASSavePasswordRequest
```

## Topics

### Initializers
- [init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, sessionID: String, event: ASSavePasswordRequest.Event)](assavepasswordrequest/init(serviceidentifier:credential:sessionid:event:).md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, sessionID: String, event: ASSavePasswordRequest.Event, passwordKind: ASGeneratedPassword.Kind?)](assavepasswordrequest/init(serviceidentifier:credential:sessionid:event:passwordkind:).md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, title: String?, sessionID: String, event: ASSavePasswordRequest.Event)](assavepasswordrequest/init(serviceidentifier:credential:title:sessionid:event:).md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, title: String?, sessionID: String, event: ASSavePasswordRequest.Event, passwordKind: ASGeneratedPassword.Kind?)](assavepasswordrequest/init(serviceidentifier:credential:title:sessionid:event:passwordkind:).md)
### Instance Properties
- [var credential: ASPasswordCredential](assavepasswordrequest/credential.md)
  The credential to save.
- [var event: ASSavePasswordRequest.Event](assavepasswordrequest/event-swift.property.md)
  The type of event that the save request represents.
- [var passwordKind: ASGeneratedPassword.Kind?](assavepasswordrequest/passwordkind.md)
  For passwordFilled events, this is the kind of password that was created.
- [var serviceIdentifier: ASCredentialServiceIdentifier](assavepasswordrequest/serviceidentifier.md)
  The identifier of the service for which the the credential should be associated.
- [var sessionID: String](assavepasswordrequest/sessionid.md)
  An ID that represents a form’s session.
- [var title: String?](assavepasswordrequest/title.md)
  A user-displayable name for the password credential to be saved.
### Enumerations
- [ASSavePasswordRequest.Event](assavepasswordrequest/event-swift.enum.md)

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest)*