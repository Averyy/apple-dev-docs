# authenticationRequired

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating if the server requires authentication credentials.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var authenticationRequired: Bool { get set }
```

```objc
@property BOOL authenticationRequired;
```

## See Also

### Accessing Proxy Server Properties
- [var address: String](./address.md)
  The address of the proxy server.
- [var port: Int](./port.md)
  The TCP port on which the proxy server is listening for connections.
- [var username: String?](./username.md)
  The username portion of the authentication credential to be used to authenticate with the proxy server.
- [var password: String?](./password.md)
  The password portion of the authentication credential to be used to authenticate with the proxy server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxyserver/authenticationrequired)*