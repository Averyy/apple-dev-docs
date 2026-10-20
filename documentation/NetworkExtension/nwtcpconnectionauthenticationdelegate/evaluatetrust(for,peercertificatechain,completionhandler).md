# evaluateTrust(for:peerCertificateChain:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Override the default trust evaluation for the connection.

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
optional func evaluateTrust(for connection: NWTCPConnection, peerCertificateChain: [Any], completionHandler completion: @escaping (SecTrust) -> Void)
```

```objc
- (void) evaluateTrustForConnection:(NWTCPConnection *) connection peerCertificateChain:(NSArray<id> *) peerCertificateChain completionHandler:(void (^)(SecTrustRef trust)) completion;
```

#### Discussion

The caller can implement this optional protocol method to set up custom policies for peer certificate trust evaluation. If the delegate method is implemented, the caller is responsible for creating and setting up the [`SecTrust`](../../Security/sectrust.md) object and passing it to the completion handler. Otherwise, the default trust evaluation policy is used for the connection.

## Parameters

- `connection`: The connection sending this message
- `peerCertificateChain`: The connection peer’s certificate chain
- `completion`: The completion handler for passing the [`SecTrust`](../../Security/sectrust.md) object to the connection. The `SecTrustRef` object `trust` is required and must not be `nil`. It will be evaluated using [`SecTrustEvaluate(_:_:)`](../../Security/sectrustevaluate%28_,_%29.md) if necessary.

  The caller is responsible for keeping the argument object valid for the duration of the completion handler invocation.

## See Also

### Delegate methods
- [func shouldEvaluateTrust(for: NWTCPConnection) -> Bool](./shouldevaluatetrust%28for%29.md)
  Indicate that the delegate should override the default trust evaluation for the connection.
- [func shouldProvideIdentity(for: NWTCPConnection) -> Bool](./shouldprovideidentity%28for%29.md)
  Indicate that the delegate can provide an identity for the connection authentication.
- [func provideIdentity(for: NWTCPConnection, completionHandler: (SecIdentity, [Any]) -> Void)](./provideidentity%28for,completionhandler%29.md)
  Provide the identity and an optional certificate chain to be used for authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/evaluatetrust(for:peercertificatechain:completionhandler:))*