# credentialWithUser:password:persistence:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a URL credential instance for internet password authentication with a given user name and password, using a given persistence setting.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSURLCredential *) credentialWithUser:(NSString *) user password:(NSString *) password persistence:(NSURLCredentialPersistence) persistence;
```

#### Return Value

A new URL credential object with user name `user`, password `password`, and using persistence setting `persistence`.

#### Discussion

If `persistence` is [`URLCredential.Persistence.permanent`](../urlcredential/persistence-swift.enum/permanent.md), the credential is stored in the keychain. If `persistence` is [`URLCredential.Persistence.synchronizable`](../urlcredential/persistence-swift.enum/synchronizable.md), it is also synchronized to the user’s other devices.

## Parameters

- `user`: The user for the credential.
- `password`: The password for `user`.
- `persistence`: A [`URLCredential.Persistence`](../urlcredential/persistence-swift.enum.md) value indicating whether the credential should be stored permanently, for the duration of the current session, or not at all.

## See Also

### Creating a credential
- [+ credentialWithIdentity:certificates:persistence:](./credentialwithidentity_certificates_persistence_.md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
- [init(identity: SecIdentity, certificates: [Any]?, persistence: URLCredential.Persistence)](../urlcredential/init%28identity,certificates,persistence%29.md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
- [init(trust: SecTrust)](../urlcredential/init%28trust%29.md)
  Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [init(user: String, password: String, persistence: URLCredential.Persistence)](../urlcredential/init%28user,password,persistence%29.md)
  Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [URLCredential.Persistence](../urlcredential/persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcredential/credentialwithuser:password:persistence:)*