# init(serviceIdentifier:credential:title:sessionID:event:passwordKind:)

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
init(serviceIdentifier: ASCredentialServiceIdentifier, credential: ASPasswordCredential, title: String?, sessionID: String, event: ASSavePasswordRequest.Event, passwordKind: ASGeneratedPassword.Kind?)
```

```objc
- (instancetype) initWithServiceIdentifier:(ASCredentialServiceIdentifier *) serviceIdentifier credential:(ASPasswordCredential *) credential title:(NSString *) title sessionID:(NSString *) sessionID event:(ASSavePasswordRequestEvent) event passwordKind:(ASGeneratedPasswordKind) passwordKind;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest/init(serviceidentifier:credential:title:sessionid:event:passwordkind:))*