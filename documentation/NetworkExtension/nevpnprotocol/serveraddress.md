# serverAddress

**Framework**: Network Extension  
**Kind**: property

The address of the VPN server.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var serverAddress: String? { get set }
```

#### Discussion

The format of the value of this property depends on the type of VPN protocol in use. For example, for IPSec the value should be a hostname or an IP address. For a custom SSL-VPN protocol the value may be a URL. The only requirement imposed by the Network Extension framework is that this property must have a non-`nil` string value for the protocol configuration to be valid.

## See Also

- [var disconnectOnSleep: Bool](nevpnprotocol/disconnectonsleep.md)
  A Boolean value that indicates whether the VPN disconnects when the device sleeps.
- [var proxySettings: NEProxySettings?](nevpnprotocol/proxysettings.md)
  The proxy settings to use for HTTP and HTTPS connections that route through the VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/serveraddress)*