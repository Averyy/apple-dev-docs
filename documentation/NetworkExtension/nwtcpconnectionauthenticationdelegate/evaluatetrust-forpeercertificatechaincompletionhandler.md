# evaluateTrust(for:peerCertificateChain:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Override the default trust evaluation for the connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func evaluateTrust(for connection: NWTCPConnection, peerCertificateChain: [Any], completionHandler completion: @escaping (SecTrust) -> Void)
```

#### Discussion

The caller can implement this optional protocol method to set up custom policies for peer certificate trust evaluation. If the delegate method is implemented, the caller is responsible for creating and setting up the [`SecTrust`](https://developer.apple.com/documentation/Security/SecTrust) object and passing it to the completion handler. Otherwise, the default trust evaluation policy is used for the connection.

## Parameters

- `connection`: The connection sending this message
- `peerCertificateChain`: The connection peer’s certificate chain
- `completion`: The caller is responsible for keeping the argument object valid for the duration of the completion handler invocation.

## See Also

- [func shouldEvaluateTrust(for: NWTCPConnection) -> Bool](nwtcpconnectionauthenticationdelegate/shouldevaluatetrust(for:).md)
  Indicate that the delegate should override the default trust evaluation for the connection.
- [func shouldProvideIdentity(for: NWTCPConnection) -> Bool](nwtcpconnectionauthenticationdelegate/shouldprovideidentity(for:).md)
  Indicate that the delegate can provide an identity for the connection authentication.
- [func provideIdentity(for: NWTCPConnection, completionHandler: (SecIdentity, [Any]) -> Void)](nwtcpconnectionauthenticationdelegate/provideidentity(for:completionhandler:).md)
  Provide the identity and an optional certificate chain to be used for authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/evaluatetrust(for:peercertificatechain:completionhandler:))*