# address

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The address of the proxy server.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var address: String { get }
```

```objc
@property (readonly) NSString * address;
```

## See Also

### Accessing Proxy Server Properties
- [var port: Int](./port.md)
  The TCP port on which the proxy server is listening for connections.
- [var authenticationRequired: Bool](./authenticationrequired.md)
  A Boolean indicating if the server requires authentication credentials.
- [var username: String?](./username.md)
  The username portion of the authentication credential to be used to authenticate with the proxy server.
- [var password: String?](./password.md)
  The password portion of the authentication credential to be used to authenticate with the proxy server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxyserver/address)*