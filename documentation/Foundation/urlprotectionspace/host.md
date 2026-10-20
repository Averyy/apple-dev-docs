# host

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s host.

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
var host: String { get }
```

```objc
@property (copy, readonly) NSString * host;
```

## Mentions

- [Performing manual server trust authentication](../performing-manual-server-trust-authentication.md)

## See Also

### Getting protection space properties
- [var authenticationMethod: String](./authenticationmethod.md)
  The authentication method used by the receiver.
- [var distinguishedNames: [Data]?](./distinguishednames.md)
  The acceptable certificate-issuing authorities for client certificate authentication.
- [var port: Int](./port.md)
  The receiver’s port.
- [var `protocol`: String?](./protocol.md)
  The receiver’s protocol.
- [var proxyType: String?](./proxytype.md)
  The receiver’s proxy type.
- [var realm: String?](./realm.md)
  The receiver’s authentication realm
- [var receivesCredentialSecurely: Bool](./receivescredentialsecurely.md)
  A Boolean value that indicates whether the credentials for the protection space can be sent securely.
- [var serverTrust: SecTrust?](./servertrust.md)
  A representation of the server’s SSL transaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotectionspace/host)*