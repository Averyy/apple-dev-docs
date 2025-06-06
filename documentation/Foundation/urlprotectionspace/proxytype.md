# proxyType

**Framework**: Foundation  
**Kind**: property

The receiver’s proxy type.

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
var proxyType: String? { get }
```

#### Discussion

This value is `nil` if the receiver does not represent a proxy protection space. The supported proxy types are listed in [`NSURLProtectionSpace proxy types`](nsurlprotectionspace-proxy-types.md).

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
- [var realm: String?](urlprotectionspace/realm.md)
  The receiver’s authentication realm
- [var receivesCredentialSecurely: Bool](urlprotectionspace/receivescredentialsecurely.md)
  A Boolean value that indicates whether the credentials for the protection space can be sent securely.
- [var serverTrust: SecTrust?](urlprotectionspace/servertrust.md)
  A representation of the server’s SSL transaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotectionspace/proxytype)*