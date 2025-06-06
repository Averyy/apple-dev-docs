# receivesCredentialSecurely

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/swift/true) if the credentials for the protection space represented by the receiver can be sent securely, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## See Also

- [var authenticationMethod: String](urlprotectionspace/authenticationmethod.md)
  The authentication method used by the receiver.
- [var distinguishedNames: [Data]?](urlprotectionspace/distinguishednames.md)
  The acceptable certificate-issuing authorities for client certificate authentication.
- [var host: String](urlprotectionspace/host.md)
  The receiver’s host.
- [var port: Int](urlprotectionspace/port.md)
  The receiver’s port.
- [var `protocol`: String?](urlprotectionspace/protocol.md)
  The receiver’s protocol.
- [var proxyType: String?](urlprotectionspace/proxytype.md)
  The receiver’s proxy type.
- [var realm: String?](urlprotectionspace/realm.md)
  The receiver’s authentication realm
- [var serverTrust: SecTrust?](urlprotectionspace/servertrust.md)
  A representation of the server’s SSL transaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotectionspace/receivescredentialsecurely)*