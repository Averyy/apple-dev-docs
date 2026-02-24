# init(proxyHost:port:type:realm:authenticationMethod:)

**Framework**: Foundation  
**Kind**: init

Creates a protection space object representing a proxy server.

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
init(proxyHost host: String, port: Int, type: String?, realm: String?, authenticationMethod: String?)
```

#### Return Value

A new protection space object, with the given host, port, proxyType, realm, and authenticationMethod.

## Parameters

- `host`: The host of the proxy server for the protection space object.
- `port`: The port for the protection space object. If `port` is 0 the default port for the specified proxy type is used, for example, port 80 for HTTP. Note that servers can, and do, treat these values differently.
- `type`: The type of proxy server. The value of `proxyType` should be set to one of the values specified in [`NSURLProtectionSpace proxy types`](nsurlprotectionspace-proxy-types.md).
- `realm`: A string indicating a protocol specific subdivision of the host. `realm` may be `nil` if there is no specified realm or if the protocol doesn’t support realms.
- `authenticationMethod`: The type of authentication to use. `authenticationMethod` should be set to one of the values in [`NSURLProtectionSpace authentication method constants`](nsurlprotectionspace-authentication-method-constants.md) or `nil` to use the default, [`NSURLAuthenticationMethodDefault`](nsurlauthenticationmethoddefault.md).

## See Also

- [init(host: String, port: Int, protocol: String?, realm: String?, authenticationMethod: String?)](urlprotectionspace/init(host:port:protocol:realm:authenticationmethod:).md)
  Creates a protection space object from the given host, port, protocol, realm, and authentication method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotectionspace/init(proxyhost:port:type:realm:authenticationmethod:))*