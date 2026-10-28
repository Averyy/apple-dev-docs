# providerProtocol

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (strong, nullable) NEDNSProxyProviderProtocol * providerProtocol;
```

## Discussion

As the author of the DNS proxy, you decide what configuration the proxy needs. For example, if your proxy requires the IP addresses of servers to which DNS traffic can be redirected, you can use an array of strings to hold these values.

Initially, you store this array in the configuration profile, as described in [Configuration Profile Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206). When you want to inspect or modify this data, you call [`loadFromPreferences(completionHandler:)`](./loadfrompreferences%28completionhandler%29.md) to pull the configuration into memory. You access this memory through the proxy manager’s [`providerProtocol`](./providerprotocol.md) property.

## See Also

### Accessing DNS proxy configuration properties
- [var isEnabled: Bool](./isenabled.md)
  The status of a DNS proxy.
- [var localizedDescription: String?](./localizeddescription.md)
  A description of the DNS proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/providerprotocol)*