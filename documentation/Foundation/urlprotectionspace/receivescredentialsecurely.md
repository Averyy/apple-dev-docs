# receivesCredentialSecurely

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the credentials for the protection space can be sent securely.

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
var receivesCredentialSecurely: Bool { get }
```

```objc
@property (readonly) BOOL receivesCredentialSecurely;
```

#### Discussion

This value is [`true`](../../Swift/true.md) if the credentials for the protection space represented by the receiver can be sent securely, [`false`](../../Swift/false.md) otherwise.

## See Also

### Getting protection space properties
- [var authenticationMethod: String](./authenticationmethod.md)
  The authentication method used by the receiver.
- [var distinguishedNames: [Data]?](./distinguishednames.md)
  The acceptable certificate-issuing authorities for client certificate authentication.
- [var host: String](./host.md)
  The receiver’s host.
- [var port: Int](./port.md)
  The receiver’s port.
- [var `protocol`: String?](./protocol.md)
  The receiver’s protocol.
- [var proxyType: String?](./proxytype.md)
  The receiver’s proxy type.
- [var realm: String?](./realm.md)
  The receiver’s authentication realm
- [var serverTrust: SecTrust?](./servertrust.md)
  A representation of the server’s SSL transaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotectionspace/receivescredentialsecurely)*