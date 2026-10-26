# URLCredential

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

`A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class URLCredential
```

```objc
@interface NSURLCredential : NSObject
```

## Mentions

- [Performing manual server trust authentication](./performing-manual-server-trust-authentication.md)

#### Overview

The URL Loading System supports password-based user credentials, certificate-based user credentials, and certificate-based server credentials.

When you create a credential, you can specify it for a single request, persist it temporarily (until your app quits), or persist it permanently. Permanent persistence can be local persistence in the keychain, or synchronized persistence across the user’s devices, based on their Apple ID.

> **Note**:  Permanent storage of credentials is only available for password-based credentials. TLS credentials are never stored permanently by [`URLCredentialStorage`](./urlcredentialstorage.md). In general, use for-session persistence for TLS credentials.

## Topics

### Creating a credential
- [init(forTrust: SecTrust)](./urlcredential/init%28fortrust%29.md)
  Creates a URL credential instance for server trust authentication with a given accepted trust.
- [init(identity: SecIdentity, certificates: [Any]?, persistence: URLCredential.Persistence)](./urlcredential/init%28identity,certificates,persistence%29.md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
- [init(trust: SecTrust)](./urlcredential/init%28trust%29.md)
  Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [init(user: String, password: String, persistence: URLCredential.Persistence)](./urlcredential/init%28user,password,persistence%29.md)
  Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [URLCredential.Persistence](./urlcredential/persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.
- [+ credentialWithUser:password:persistence:](./nsurlcredential/credentialwithuser_password_persistence_.md)
  Creates a URL credential instance for internet password authentication with a given user name and password, using a given persistence setting.
- [+ credentialWithIdentity:certificates:persistence:](./nsurlcredential/credentialwithidentity_certificates_persistence_.md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
### Getting credential properties
- [var user: String?](./urlcredential/user.md)
  The credential’s user name.
- [var certificates: [Any]](./urlcredential/certificates.md)
  The intermediate certificates of the credential, if it is a client certificate credential.
- [var hasPassword: Bool](./urlcredential/haspassword.md)
  A Boolean value that indicates whether the credential has a password.
- [var password: String?](./urlcredential/password.md)
  The credential’s password.
- [var identity: SecIdentity?](./urlcredential/identity.md)
  The identity of this credential if it is a client certificate credential.
- [var persistence: URLCredential.Persistence](./urlcredential/persistence-swift.property.md)
  The credential’s persistence setting.
- [URLCredential.Persistence](./urlcredential/persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.
### Initializers
- [init?(coder: NSCoder)](./urlcredential/init%28coder%29.md)
### Default Implementations
- [NSURLCredential Implementations](./urlcredential/nsurlcredential-implementations.md)
### Type Methods
- [+ credentialForTrust:](./nsurlcredential/credentialfortrust_.md)
  Creates a URL credential instance for server trust authentication with a given accepted trust.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Authentication and credentials
- [Handling an authentication challenge](./handling-an-authentication-challenge.md)
  Respond appropriately when a server demands authentication for a URL request.
- [class URLAuthenticationChallenge](./urlauthenticationchallenge.md)
  A challenge from a server requiring authentication from the client.
- [class URLCredentialStorage](./urlcredentialstorage.md)
  The manager of a shared credentials cache.
- [class URLProtectionSpace](./urlprotectionspace.md)
  A server or an area on a server, commonly referred to as a realm, that requires authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential)*