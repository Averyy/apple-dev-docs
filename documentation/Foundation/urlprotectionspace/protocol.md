# protocol

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s protocol.

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
var `protocol`: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * protocol;
```

#### Discussion

This value is `nil` if the receiver represents a proxy protection space.

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
- [var proxyType: String?](./proxytype.md)
  The receiver’s proxy type.
- [var realm: String?](./realm.md)
  The receiver’s authentication realm
- [var receivesCredentialSecurely: Bool](./receivescredentialsecurely.md)
  A Boolean value that indicates whether the credentials for the protection space can be sent securely.
- [var serverTrust: SecTrust?](./servertrust.md)
  A representation of the server’s SSL transaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotectionspace/protocol)*