# serverTrust

**Framework**: Foundation  
**Kind**: property

A representation of the server’s SSL transaction state.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var serverTrust: SecTrust? { get }
```

## Mentions

- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md)

#### Discussion

This value is `nil` if the authentication method of the protection space is not server trust.

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
- [var receivesCredentialSecurely: Bool](urlprotectionspace/receivescredentialsecurely.md)
  A Boolean value that indicates whether the credentials for the protection space can be sent securely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotectionspace/servertrust)*