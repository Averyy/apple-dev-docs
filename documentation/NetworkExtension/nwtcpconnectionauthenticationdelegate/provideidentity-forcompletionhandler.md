# provideIdentity(for:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Provide the identity and an optional certificate chain to be used for authentication.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func provideIdentity(for connection: NWTCPConnection, completionHandler completion: @escaping (SecIdentity, [Any]) -> Void)
```

#### Discussion

Optional. If this method is not implemented, the default certificate evaluation will be used.

## Parameters

- `connection`: The connection sending this message
- `completion`: The caller is responsible for keeping the argument object(s) valid for the duration of the completion handler invocation.

## See Also

- [func shouldEvaluateTrust(for: NWTCPConnection) -> Bool](nwtcpconnectionauthenticationdelegate/shouldevaluatetrust(for:).md)
  Indicate that the delegate should override the default trust evaluation for the connection.
- [func evaluateTrust(for: NWTCPConnection, peerCertificateChain: [Any], completionHandler: (SecTrust) -> Void)](nwtcpconnectionauthenticationdelegate/evaluatetrust(for:peercertificatechain:completionhandler:).md)
  Override the default trust evaluation for the connection.
- [func shouldProvideIdentity(for: NWTCPConnection) -> Bool](nwtcpconnectionauthenticationdelegate/shouldprovideidentity(for:).md)
  Indicate that the delegate can provide an identity for the connection authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/provideidentity(for:completionhandler:))*