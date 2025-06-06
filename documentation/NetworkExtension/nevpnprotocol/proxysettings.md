# proxySettings

**Framework**: Network Extension  
**Kind**: property

The proxy settings to use for HTTP and HTTPS connections that route through the VPN.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var proxySettings: NEProxySettings? { get set }
```

#### Discussion

While operating under an established VPN tunnel, HTTP and HTTPS connections inside the tunnel use the given proxy settings.

## See Also

- [var serverAddress: String?](nevpnprotocol/serveraddress.md)
  The address of the VPN server.
- [var disconnectOnSleep: Bool](nevpnprotocol/disconnectonsleep.md)
  A Boolean value that indicates whether the VPN disconnects when the device sleeps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/proxysettings)*