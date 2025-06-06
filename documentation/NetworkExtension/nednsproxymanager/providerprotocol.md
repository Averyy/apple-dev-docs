# providerProtocol

**Framework**: Network Extension  
**Kind**: property

The provider-specific portion of the DNS proxy configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var providerProtocol: NEDNSProxyProviderProtocol? { get set }
```

#### Discussion

As the author of the DNS proxy, you decide what configuration the proxy needs. For example, if your proxy requires the IP addresses of servers to which DNS traffic can be redirected, you can use an array of strings to hold these values.

Initially, you store this array in the configuration profile, as described in [`Configuration Profile Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206). When you want to inspect or modify this data, you call [`loadFromPreferences(completionHandler:)`](nednsproxymanager/loadfrompreferences(completionhandler:).md) to pull the configuration into memory. You access this memory through the proxy manager’s [`providerProtocol`](nednsproxymanager/providerprotocol.md) property.

## See Also

- [var isEnabled: Bool](nednsproxymanager/isenabled.md)
  The status of a DNS proxy.
- [var localizedDescription: String?](nednsproxymanager/localizeddescription.md)
  A description of the DNS proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/providerprotocol)*