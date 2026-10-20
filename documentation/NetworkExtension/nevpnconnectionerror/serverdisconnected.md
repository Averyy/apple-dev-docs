# NEVPNConnectionError.serverDisconnected

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

An error code that indicates the VPN connection failed because the VPN server terminated the connection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case serverDisconnected
```

```c
NEVPNConnectionErrorServerDisconnected
```

## See Also

### VPN server error codes
- [NEVPNConnectionError.serverAddressResolutionFailed](./serveraddressresolutionfailed.md)
  An error code that indicates the VPN connection failed because the system couldn’t determine the VPN server address.
- [NEVPNConnectionError.serverNotResponding](./servernotresponding.md)
  An error code that indicates the VPN connection failed because the VPN server isn’t responding.
- [NEVPNConnectionError.serverDead](./serverdead.md)
  An error code that indicates the VPN connection failed because the VPN server has stopped responding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnectionerror/serverdisconnected)*