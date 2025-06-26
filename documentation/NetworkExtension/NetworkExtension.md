# Network Extension

**Framework**: Network Extension  
**Kind**: module

Customize and extend core networking features.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 7.0+

#### Overview

With the NetworkExtension framework, you can customize and extend the system’s core networking features. Specifically, you can:

- Change the system’s Wi-Fi configuration
- Integrate your app with the hotspot network subsystem (Hotspot Helper)
- Create and manage VPN configurations, using the built-in VPN protocols (Personal VPN) or a custom VPN protocol
- Create and manage network relay configurations
- Implement an on-device content filter
- Create and manage system-wide DNS configurations, using the built-in DNS protocols or a custom on-device DNS proxy

The NetworkExtension framework is available in macOS, iOS, tvOS, and visionOS, but not all features are available on all platforms and some features have specific restrictions (for example, some features only work on supervised iOS devices). The documentation for each feature describes these restrictions.

##### Options for Implementing Vpn

The NetworkExtension framework has extensive support for virtual private networks (VPN).  A VPN is a form of network tunnel, where a VPN client uses the public Internet to create a connection to a VPN server and then passes private network traffic over that connection.

VPNs have many different uses.  For example, an enterprise might set up a VPN to give remote employees access to enterprise network resources that are not available on the public Internet.  Or a consumer wanting to access the Internet from an untrusted network, such as the free Wi-Fi at an airport, might set up VPN to secure their traffic.

The supported operating systems include a number of different VPN APIs, distinguished by the protocols they support:

- Use [`Personal VPN`](personal-vpn.md) to create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).
- Create a [`Packet tunnel provider`](packet-tunnel-provider.md) to implement a VPN client for a packet-oriented, custom VPN protocol.
- Create an [`App proxy provider`](app-proxy-provider.md) to implement a VPN client for a flow-oriented, custom VPN protocol.

##### About Always on Vpn

iOS supports Always-on VPN to ensure all IP traffic is tunneled back to the organization. See the [`iOS Deployment Reference`](https://developer.apple.comhttps://support.apple.com/guide/deployment-reference-ios/always-on-vpn-iore8b083096/1/web/1) for information about how to configure Always-on VPN.

## Topics

### Wi-Fi management
- [Wi-Fi configuration](wi-fi-configuration.md)
  Add persistent Wi-Fi configurations, or temporarily move the device to a specific Wi-Fi network.
- [Configuring a Wi-Fi accessory to join a network](configuring-a-wi-fi-accessory-to-join-a-network.md)
  Associate an iOS device with an accessory’s network to deliver network configuration information.
- [Hotspot helper](hotspot-helper.md)
  Integrate your app with the iOS hotspot network subsystem.
### Virtual private networks
- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)
  Configure your VPN to include and exclude some network traffic.
- [Personal VPN](personal-vpn.md)
  Create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).
- [Packet tunnel provider](packet-tunnel-provider.md)
  Implement a VPN client for a packet-oriented, custom VPN protocol.
- [App proxy provider](app-proxy-provider.md)
  Implement a VPN client for a flow-oriented, custom VPN protocol.
### Network relays
- [Relays](relays.md)
  Create and manage a system-wide network relay configuration that uses built-in proxying for TCP and UDP traffic over HTTP/3 and HTTP/2.
### Content filters
- [Content filter providers](content-filter-providers.md)
  Create an on-device network content filter.
- [Filtering Network Traffic](filtering-network-traffic.md)
  Use the Network Extension framework to allow or deny network connections.
### URL filters
- [URL filters](url-filters.md)
  Create a filter that analyzes full URLs, while preserving privacy.
### DNS configurations
- [DNS settings](dns-settings.md)
  Create and manage a system-wide DNS configuration that uses built-in encrypted DNS protocols.
- [DNS proxy provider](dns-proxy-provider.md)
  Create an on-device DNS proxy using a custom protocol.
### Local networking
- [Local push connectivity](local-push-connectivity.md)
  Provide functionality similar to Apple Push Notification Service when access to the wider internet is unavailable.
### App extensions
- [class NEAppExtensionConfiguration](neappextensionconfiguration.md)
  A class that defines configuration options for use in NetworkExtension app extensions.
### Classes
- [class NEVPNIKEv2PPKConfiguration](nevpnikev2ppkconfiguration.md)
### Protocols
- [protocol NEAppProxyUDPFlowHandling](neappproxyudpflowhandling.md)
### Structures
- [struct NETunnelProviderError](netunnelprovidererror-swift.struct.md)
  An error that the tunnel provider encounters.
- [struct NEVPNError](nevpnerror-swift.struct.md)
  Information about an error encountered while configuring or using a VPN.
### Variables
- [let NERelayClientErrorDomain: String](nerelayclienterrordomain.md)
### Enumerations
- [enum NERelayManagerClientError](nerelaymanagerclienterror.md)
- [enum NEVPNIKEv2PostQuantumKeyExchangeMethod](nevpnikev2postquantumkeyexchangemethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/NetworkExtension)*