# shouldEvaluateTrust(for:)

**Framework**: Network Extension  
**Kind**: method

Indicate that the delegate should override the default trust evaluation for the connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func shouldEvaluateTrust(for connection: NWTCPConnection) -> Bool
```

#### Return Value

Return [`true`](https://developer.apple.com/documentation/swift/true) to take over the default trust evaluation, in which case the delegate method `evaluateTrustForConnection:peerCertificateChain:completionHandler`: will be called.

#### Discussion

The caller can implement this optional protocol method to decide whether it wants to take over the default trust evaluation for this connection. If this delegate method is not implemented, the return value will default to YES if  `provideIdentityForConnection:completionHandler:` is implemented.

## Parameters

- `connection`: The connection sending this message

## See Also

- [func evaluateTrust(for: NWTCPConnection, peerCertificateChain: [Any], completionHandler: (SecTrust) -> Void)](nwtcpconnectionauthenticationdelegate/evaluatetrust(for:peercertificatechain:completionhandler:).md)
  Override the default trust evaluation for the connection.
- [func shouldProvideIdentity(for: NWTCPConnection) -> Bool](nwtcpconnectionauthenticationdelegate/shouldprovideidentity(for:).md)
  Indicate that the delegate can provide an identity for the connection authentication.
- [func provideIdentity(for: NWTCPConnection, completionHandler: (SecIdentity, [Any]) -> Void)](nwtcpconnectionauthenticationdelegate/provideidentity(for:completionhandler:).md)
  Provide the identity and an optional certificate chain to be used for authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/shouldevaluatetrust(for:))*