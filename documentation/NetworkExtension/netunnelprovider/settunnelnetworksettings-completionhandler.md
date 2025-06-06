# setTunnelNetworkSettings(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Specify the network settings for the current tunneling session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setTunnelNetworkSettings(_ tunnelNetworkSettings: NETunnelNetworkSettings?) async throws
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Discussion

Use this method to specify the settings to be used by network communication that traverses the tunnel. If you are implementing a Packet Tunnel Provider, pass a [`NEPacketTunnelNetworkSettings`](nepackettunnelnetworksettings.md) object containing virtual IP configuration, DNS settings, proxy settings, the tunnel MTU, and IP routes. If you are implementing an App Proxy Provider, pass a [`NETunnelNetworkSettings`](netunnelnetworksettings.md) containing DNS settings and proxy settings.

This method should be called as part of the process of establishing the tunnel, as follows:

- The system calls the appropriate “start” method on the tunnel provider object.
- The provider obtains the network settings for the tunnel by some means dictated by the tunnel provider, such as by downloading them from the tunnel server.
- The tunnel provider calls [`setTunnelNetworkSettings(_:completionHandler:)`](netunnelprovider/settunnelnetworksettings(_:completionhandler:).md) method to apply the network settings to the system.
- The system executes the completion handler passed to `setTunnelNetworkSettings:completionHandler`: to indicate that the network settings have been set.
- The tunnel provider executes the completion handler block passed to the “start” method to indicate that the tunnel is fully established.

## Parameters

- `tunnelNetworkSettings`: The network settings to use for the tunnel. Pass nil to clear out the network settings for the current tunneling session.
- `completionHandler`: A block that will be executed when the operation of setting the network settings is complete. If the network settings could not be set due to an error, then the error parameter will be set to an   object containing more information about the error. See   for possible error codes. If the network settings were set successfully then the error parameter will be set to nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovider/settunnelnetworksettings(_:completionhandler:))*