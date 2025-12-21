# shouldProvideIdentity(for:)

**Framework**: Network Extension  
**Kind**: method

Indicate that the delegate can provide an identity for the connection authentication.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func shouldProvideIdentity(for connection: NWTCPConnection) -> Bool
```

#### Return Value

Return [`true`](https://developer.apple.com/documentation/Swift/true) to provide the identity for this connection, in which case the delegate method [`provideIdentity(for:completionHandler:)`](nwtcpconnectionauthenticationdelegate/provideidentity(for:completionhandler:).md) will be called.

#### Discussion

The caller can implement this optional protocol method to decide whether it wants to provide the identity for this connection for authentication. If this delegate method is not implemented, the return value will default to YES if [`provideIdentity(for:completionHandler:)`](nwtcpconnectionauthenticationdelegate/provideidentity(for:completionhandler:).md) is implemented.

## Parameters

- `connection`: The connection sending this message.

## See Also

- [func shouldEvaluateTrust(for: NWTCPConnection) -> Bool](nwtcpconnectionauthenticationdelegate/shouldevaluatetrust(for:).md)
  Indicate that the delegate should override the default trust evaluation for the connection.
- [func evaluateTrust(for: NWTCPConnection, peerCertificateChain: [Any], completionHandler: (SecTrust) -> Void)](nwtcpconnectionauthenticationdelegate/evaluatetrust(for:peercertificatechain:completionhandler:).md)
  Override the default trust evaluation for the connection.
- [func provideIdentity(for: NWTCPConnection, completionHandler: (SecIdentity, [Any]) -> Void)](nwtcpconnectionauthenticationdelegate/provideidentity(for:completionhandler:).md)
  Provide the identity and an optional certificate chain to be used for authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/shouldprovideidentity(for:))*