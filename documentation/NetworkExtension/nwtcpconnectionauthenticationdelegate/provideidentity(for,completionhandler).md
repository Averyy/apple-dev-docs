# provideIdentity(for:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Provide the identity and an optional certificate chain to be used for authentication.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`sec_protocol_options_set_challenge_block(_:_:_:)`](../../Security/sec_protocol_options_set_challenge_block%28_,_,_%29.md) function from the [Security](../../Security/Security.md) framework instead.

## Declaration

```swift
optional func provideIdentity(for connection: NWTCPConnection, completionHandler completion: @escaping (SecIdentity, [Any]) -> Void)
```

```objc
- (void) provideIdentityForConnection:(NWTCPConnection *) connection completionHandler:(void (^)(SecIdentityRef identity, NSArray<id> *certificateChain)) completion;
```

## Discussion

Optional. If this method is not implemented, the default certificate evaluation will be used.

## Parameters

- `connection`: The connection sending this message
- `completion`: The completion handler for passing an identity and certificate chain to the connection. The `identity` is required and must not be `nil`. The `certificateChain` argument is optional, and is an array of one or more [`SecCertificate`](../../Security/seccertificate.md) objects. The certificate chain must contain objects of type `SecCertificateRef` only. If the certificate chain is set, it will be used. Otherwise, the leaf certificate will be extracted from the [`SecIdentity`](../../Security/secidentity.md) object and will be used for authentication.

  The caller is responsible for keeping the argument object(s) valid for the duration of the completion handler invocation.

## See Also

### Delegate methods
- [func shouldEvaluateTrust(for: NWTCPConnection) -> Bool](./shouldevaluatetrust%28for%29.md)
  Indicate that the delegate should override the default trust evaluation for the connection.
- [func evaluateTrust(for: NWTCPConnection, peerCertificateChain: [Any], completionHandler: (SecTrust) -> Void)](./evaluatetrust%28for,peercertificatechain,completionhandler%29.md)
  Override the default trust evaluation for the connection.
- [func shouldProvideIdentity(for: NWTCPConnection) -> Bool](./shouldprovideidentity%28for%29.md)
  Indicate that the delegate can provide an identity for the connection authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/provideidentity(for:completionhandler:))*