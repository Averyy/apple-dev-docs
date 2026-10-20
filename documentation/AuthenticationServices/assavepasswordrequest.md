# ASSavePasswordRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
class ASSavePasswordRequest
```

```objc
@interface ASSavePasswordRequest : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./assavepasswordrequest/init%28coder%29.md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, sessionID: String, event: ASSavePasswordRequest.Event)](./assavepasswordrequest/init%28serviceidentifier,credential,sessionid,event%29.md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, sessionID: String, event: ASSavePasswordRequest.Event, passwordKind: ASGeneratedPassword.Kind?)](./assavepasswordrequest/init%28serviceidentifier,credential,sessionid,event,passwordkind%29.md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, title: String?, sessionID: String, event: ASSavePasswordRequest.Event)](./assavepasswordrequest/init%28serviceidentifier,credential,title,sessionid,event%29.md)
- [init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, title: String?, sessionID: String, event: ASSavePasswordRequest.Event, passwordKind: ASGeneratedPassword.Kind?)](./assavepasswordrequest/init%28serviceidentifier,credential,title,sessionid,event,passwordkind%29.md)
### Instance Properties
- [var credential: ASPasswordCredential](./assavepasswordrequest/credential.md)
  The credential to save.
- [var event: ASSavePasswordRequest.Event](./assavepasswordrequest/event-swift.property.md)
  The type of event that the save request represents.
- [var passwordKind: ASGeneratedPassword.Kind?](./assavepasswordrequest/passwordkind.md)
  For passwordFilled events, this is the kind of password that was created.
- [var serviceIdentifier: ASCredentialServiceIdentifier](./assavepasswordrequest/serviceidentifier.md)
  The identifier of the service for which the the credential should be associated.
- [var sessionID: String](./assavepasswordrequest/sessionid.md)
  An ID that represents a form’s session.
- [var title: String?](./assavepasswordrequest/title.md)
  A user-displayable name for the password credential to be saved.
### Enumerations
- [ASSavePasswordRequest.Event](./assavepasswordrequest/event-swift.enum.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest)*