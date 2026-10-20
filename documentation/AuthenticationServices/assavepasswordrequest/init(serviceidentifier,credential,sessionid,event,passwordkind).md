# init(serviceIdentifier:credential:sessionID:event:passwordKind:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, sessionID: String, event: ASSavePasswordRequest.Event, passwordKind: ASGeneratedPassword.Kind?)
```

```objc
- (instancetype) initWithServiceIdentifier:(ASCredentialServiceIdentifier *) serviceIdentifier credential:(ASPasswordCredential *) credential sessionID:(NSString *) sessionID event:(ASSavePasswordRequestEvent) event passwordKind:(ASGeneratedPasswordKind) passwordKind;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest/init(serviceidentifier:credential:sessionid:event:passwordkind:))*