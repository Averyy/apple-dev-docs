# NEVPNConnectionError.overslept

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

An error code that indicates the system slept for an extended period of time, causing the VPN connection to terminate.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case overslept
```

```c
NEVPNConnectionErrorOverslept
```

## See Also

### General error codes
- [NEVPNConnectionError.noNetworkAvailable](./nonetworkavailable.md)
  An error code that indicates the VPN connection failed because the system isn’t connected to a network.
- [NEVPNConnectionError.unrecoverableNetworkChange](./unrecoverablenetworkchange.md)
  An error code that indicates network conditions changed such that the VPN connection needed to terminate.
- [NEVPNConnectionError.configurationFailed](./configurationfailed.md)
  An error code that indicates the VPN connection failed because the configuration is invalid.
- [NEVPNConnectionError.authenticationFailed](./authenticationfailed.md)
  An error code that indicates the VPN connection failed because the VPN server rejected the user credentials.
- [NEVPNConnectionError.configurationNotFound](./configurationnotfound.md)
  An error code that indicates the VPN connection failed because the system couldn’t find a configuration.
- [NEVPNConnectionError.negotiationFailed](./negotiationfailed.md)
  An error code that indicates the VPN connection failed because the negotiation failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnectionerror/overslept)*