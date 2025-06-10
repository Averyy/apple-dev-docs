# URLProtectionSpace

**Framework**: Foundation  
**Kind**: class

A server or an area on a server, commonly referred to as a realm, that requires authentication.

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
class URLProtectionSpace
```

#### Overview

A protection space defines a series of matching constraints that determine which credential should be provided. For example, if a request provides your delegate with a [`URLAuthenticationChallenge`](urlauthenticationchallenge.md) object that requests a client username and password, your app should provide the correct username and password for the particular host, port, protocol, and realm, as specified in the challenge’s protection space.

> **Note**:  This class has no designated initializer; its `init` method always returns `nil`. You must initialize this class by calling one of the initialization methods described in Creating a protection space.

## Topics

### Creating a protection space
- [init(host: String, port: Int, protocol: String?, realm: String?, authenticationMethod: String?)](urlprotectionspace/init(host:port:protocol:realm:authenticationmethod:).md)
  Creates a protection space object from the given host, port, protocol, realm, and authentication method.
- [init(proxyHost: String, port: Int, type: String?, realm: String?, authenticationMethod: String?)](urlprotectionspace/init(proxyhost:port:type:realm:authenticationmethod:).md)
  Creates a protection space object representing a proxy server.
### Getting protection space properties
- [var authenticationMethod: String](urlprotectionspace/authenticationmethod.md)
  The authentication method used by the receiver.
- [var distinguishedNames: [Data]?](urlprotectionspace/distinguishednames.md)
  The acceptable certificate-issuing authorities for client certificate authentication.
- [var host: String](urlprotectionspace/host.md)
  The receiver’s host.
- [var port: Int](urlprotectionspace/port.md)
  The receiver’s port.
- [var `protocol`: String?](urlprotectionspace/protocol.md)
  The receiver’s protocol.
- [var proxyType: String?](urlprotectionspace/proxytype.md)
  The receiver’s proxy type.
- [var realm: String?](urlprotectionspace/realm.md)
  The receiver’s authentication realm
- [var receivesCredentialSecurely: Bool](urlprotectionspace/receivescredentialsecurely.md)
  A Boolean value that indicates whether the credentials for the protection space can be sent securely.
- [var serverTrust: SecTrust?](urlprotectionspace/servertrust.md)
  A representation of the server’s SSL transaction state.
### Identifying protection space properties
- [NSURLProtectionSpace protocol types](nsurlprotectionspace-protocol-types.md)
  These constants describe the supported protocols for a protection space, as returned by [`protocol`](urlprotectionspace/protocol.md).
- [NSURLProtectionSpace proxy types](nsurlprotectionspace-proxy-types.md)
  These constants describe the supported proxy types used in [`init(proxyHost:port:type:realm:authenticationMethod:)`](urlprotectionspace/init(proxyhost:port:type:realm:authenticationmethod:).md) and returned by [`proxyType`](urlprotectionspace/proxytype.md).
- [NSURLProtectionSpace authentication method constants](nsurlprotectionspace-authentication-method-constants.md)
  Constants describing known values of the [`authenticationMethod`](urlprotectionspace/authenticationmethod.md) property of a [`URLProtectionSpace`](urlprotectionspace.md).
### Instance Methods
- [func isProxy() -> Bool](urlprotectionspace/isproxy.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Handling an authentication challenge](handling-an-authentication-challenge.md)
  Respond appropriately when a server demands authentication for a URL request.
- [class URLAuthenticationChallenge](urlauthenticationchallenge.md)
  A challenge from a server requiring authentication from the client.
- [class URLCredential](urlcredential.md)
  `A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.
- [class URLCredentialStorage](urlcredentialstorage.md)
  The manager of a shared credentials cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotectionspace)*