# disconnectOnSleep

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL disconnectOnSleep;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the VPN
- [var serverAddress: String?](./serveraddress.md)
  The address of the VPN server.
- [var proxySettings: NEProxySettings?](./proxysettings.md)
  The proxy settings to use for HTTP and HTTPS connections that route through the VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/disconnectonsleep)*