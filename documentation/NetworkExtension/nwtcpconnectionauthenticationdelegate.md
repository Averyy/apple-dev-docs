# NWTCPConnectionAuthenticationDelegate

**Framework**: Network Extension  
**Kind**: protocol  
**Role**: Protocol

A delegate protocol to customize the TLS authentication done by a connection.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`sec_protocol_options_t`](../Security/sec_protocol_options_t.md) type from the [Security](../Security/Security.md) framework instead.

## Declaration

```swift
protocol NWTCPConnectionAuthenticationDelegate : NSObjectProtocol
```

```objc
@protocol NWTCPConnectionAuthenticationDelegate <NSObject>
```

## Overview

A delegate is not required for an [`NWTCPConnection`](./nwtcpconnection.md) object.

## Topics

### Delegate methods
- [func shouldEvaluateTrust(for: NWTCPConnection) -> Bool](./nwtcpconnectionauthenticationdelegate/shouldevaluatetrust%28for%29.md)
  Indicate that the delegate should override the default trust evaluation for the connection.
- [func evaluateTrust(for: NWTCPConnection, peerCertificateChain: [Any], completionHandler: (SecTrust) -> Void)](./nwtcpconnectionauthenticationdelegate/evaluatetrust%28for,peercertificatechain,completionhandler%29.md)
  Override the default trust evaluation for the connection.
- [func shouldProvideIdentity(for: NWTCPConnection) -> Bool](./nwtcpconnectionauthenticationdelegate/shouldprovideidentity%28for%29.md)
  Indicate that the delegate can provide an identity for the connection authentication.
- [func provideIdentity(for: NWTCPConnection, completionHandler: (SecIdentity, [Any]) -> Void)](./nwtcpconnectionauthenticationdelegate/provideidentity%28for,completionhandler%29.md)
  Provide the identity and an optional certificate chain to be used for authentication.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### TCP connections
- [class NWTCPConnection](./nwtcpconnection.md)
  An object to manage a TCP connection, with or without TLS.
- [class NWTLSParameters](./nwtlsparameters.md)
  TLS properties for creating a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate)*