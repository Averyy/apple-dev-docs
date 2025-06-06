# DNS proxy provider

**Framework**: Network Extension

Create an on-device DNS proxy using a custom protocol.

#### Overview

A DNS proxy provider is an app extension that implements DNS proxying. You should create a DNS proxy provider if you want to take responsibility for resolving all DNS queries on the system. Typically this involves forwarding the queries in a way that improves performance, reliability or security. For example, a DNS proxy provider might:

- Forward DNS queries to a well-known Internet-wide DNS server
- Talk to a DNS proxying service using DNS over HTTPS (DoH) or DNS over TLS (DoT)
- Implement a completely custom DNS proxying protocol

For detailed information about DNS proxy provider deployment options, see [`TN3134: Network Extension provider deployment`](https://developer.apple.com/documentation/Technotes/tn3134-network-extension-provider-deployment).

## Topics

### Essentials
- [Network Extensions Entitlement](../BundleResources/Entitlements/com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
### Provider
- [class NEDNSProxyProvider](nednsproxyprovider.md)
  The principal class for a DNS proxy provider app extension.
- [class NEDNSSettings](nednssettings.md)
  The DNS resolver settings of a network tunnel or a system-wide configuration.
### Handling flows
- [class NEAppProxyTCPFlow](neappproxytcpflow.md)
  An object for reading and writing data to and from a TCP connection being proxied by the provider.
- [class NEAppProxyUDPFlow](neappproxyudpflow.md)
  An object for reading and writing data to and from a UDP conversation being proxied by the provider.
- [class NEAppProxyFlow](neappproxyflow.md)
  An abstract base class shared by NEAppProxyTCPFlow and NEAppProxyUDPFlow.
### Configuration
- [class NEDNSProxyManager](nednsproxymanager.md)
  An object to create and manage an DNS proxy provider’s configuration.
- [class NEDNSProxyProviderProtocol](nednsproxyproviderprotocol.md)
  Configuration parameters for a DNS proxy.

## See Also

- [DNS settings](dns-settings.md)
  Create and manage a system-wide DNS configuration that uses built-in encrypted DNS protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/dns-proxy-provider)*