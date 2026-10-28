# NEProxyServer

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

`NEProxyServer` contains settings for a proxy server.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEProxyServer
```

```objc
@interface NEProxyServer : NSObject
```

## Overview

`NEProxyServer` instances are used inside of [`NEProxySettings`](./neproxysettings.md) instances to configure proxy settings for VPN connections.

## Topics

### Initializing a Proxy Server
- [init(address: String, port: Int)](./neproxyserver/init%28address,port%29.md)
  Initialize a newly-allocated `NEProxyServer` object
### Accessing Proxy Server Properties
- [var address: String](./neproxyserver/address.md)
  The address of the proxy server.
- [var port: Int](./neproxyserver/port.md)
  The TCP port on which the proxy server is listening for connections.
- [var authenticationRequired: Bool](./neproxyserver/authenticationrequired.md)
  A Boolean indicating if the server requires authentication credentials.
- [var username: String?](./neproxyserver/username.md)
  The username portion of the authentication credential to be used to authenticate with the proxy server.
- [var password: String?](./neproxyserver/password.md)
  The password portion of the authentication credential to be used to authenticate with the proxy server.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Accessing Manual Proxy Properties
- [var httpEnabled: Bool](./neproxysettings/httpenabled.md)
  A Boolean indicating if a static HTTP proxy will be used.
- [var httpServer: NEProxyServer?](./neproxysettings/httpserver.md)
  An [`NEProxyServer`](./neproxyserver.md) object containing the static HTTP proxy server settings.
- [var httpsEnabled: Bool](./neproxysettings/httpsenabled.md)
  A Boolean indicating if a static HTTPS proxy will be used.
- [var httpsServer: NEProxyServer?](./neproxysettings/httpsserver.md)
  An [`NEProxyServer`](./neproxyserver.md) object containing the static HTTPS proxy server settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxyserver)*