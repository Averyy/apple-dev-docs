# shouldEvaluateTrust(for:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Indicate that the delegate should override the default trust evaluation for the connection.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`sec_protocol_options_set_verify_block(_:_:_:)`](../../Security/sec_protocol_options_set_verify_block%28_,_,_%29.md) function from the [Security](../../Security/Security.md) framework instead.

## Declaration

```swift
optional func shouldEvaluateTrust(for connection: NWTCPConnection) -> Bool
```

```objc
- (BOOL) shouldEvaluateTrustForConnection:(NWTCPConnection *) connection;
```

#### Return Value

Return [`true`](../../Swift/true.md) to take over the default trust evaluation, in which case the delegate method `evaluateTrustForConnection:peerCertificateChain:completionHandler`: will be called.

#### Discussion

The caller can implement this optional protocol method to decide whether it wants to take over the default trust evaluation for this connection. If this delegate method is not implemented, the return value will default to YES if  `provideIdentityForConnection:completionHandler:` is implemented.

## Parameters

- `connection`: The connection sending this message

## See Also

### Delegate methods
- [func evaluateTrust(for: NWTCPConnection, peerCertificateChain: [Any], completionHandler: (SecTrust) -> Void)](./evaluatetrust%28for,peercertificatechain,completionhandler%29.md)
  Override the default trust evaluation for the connection.
- [func shouldProvideIdentity(for: NWTCPConnection) -> Bool](./shouldprovideidentity%28for%29.md)
  Indicate that the delegate can provide an identity for the connection authentication.
- [func provideIdentity(for: NWTCPConnection, completionHandler: (SecIdentity, [Any]) -> Void)](./provideidentity%28for,completionhandler%29.md)
  Provide the identity and an optional certificate chain to be used for authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/shouldevaluatetrust(for:))*