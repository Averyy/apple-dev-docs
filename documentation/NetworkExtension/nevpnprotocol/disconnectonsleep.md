# disconnectOnSleep

**Framework**: Network Extension  
**Kind**: property

A Boolean value that indicates whether the VPN disconnects when the device sleeps.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var disconnectOnSleep: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var serverAddress: String?](nevpnprotocol/serveraddress.md)
  The address of the VPN server.
- [var proxySettings: NEProxySettings?](nevpnprotocol/proxysettings.md)
  The proxy settings to use for HTTP and HTTPS connections that route through the VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/disconnectonsleep)*