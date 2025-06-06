# NWTCPConnectionAuthenticationDelegate

**Framework**: Network Extension  
**Kind**: protocol

A delegate protocol to customize the TLS authentication done by a connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
protocol NWTCPConnectionAuthenticationDelegate : NSObjectProtocol
```

#### Overview

A delegate is not required for an [`NWTCPConnection`](nwtcpconnection.md) object.

## Topics

### Delegate methods
- [func shouldEvaluateTrust(for: NWTCPConnection) -> Bool](nwtcpconnectionauthenticationdelegate/shouldevaluatetrust(for:).md)
  Indicate that the delegate should override the default trust evaluation for the connection.
- [func evaluateTrust(for: NWTCPConnection, peerCertificateChain: [Any], completionHandler: (SecTrust) -> Void)](nwtcpconnectionauthenticationdelegate/evaluatetrust(for:peercertificatechain:completionhandler:).md)
  Override the default trust evaluation for the connection.
- [func shouldProvideIdentity(for: NWTCPConnection) -> Bool](nwtcpconnectionauthenticationdelegate/shouldprovideidentity(for:).md)
  Indicate that the delegate can provide an identity for the connection authentication.
- [func provideIdentity(for: NWTCPConnection, completionHandler: (SecIdentity, [Any]) -> Void)](nwtcpconnectionauthenticationdelegate/provideidentity(for:completionhandler:).md)
  Provide the identity and an optional certificate chain to be used for authentication.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NWTCPConnection](nwtcpconnection.md)
  An object to manage a TCP connection, with or without TLS.
- [class NWTLSParameters](nwtlsparameters.md)
  TLS properties for creating a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate)*