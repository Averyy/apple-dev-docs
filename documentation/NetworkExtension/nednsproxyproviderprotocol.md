# NEDNSProxyProviderProtocol

**Framework**: Network Extension  
**Kind**: class

Configuration parameters for a DNS proxy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
class NEDNSProxyProviderProtocol
```

## Topics

### Accessing the DNS proxy configuration
- [var providerConfiguration: [String : Any]?](nednsproxyproviderprotocol/providerconfiguration.md)
  A dictionary containing vendor-specific configuration parameters for a proxy provider.
- [var providerBundleIdentifier: String?](nednsproxyproviderprotocol/providerbundleidentifier.md)
  A string containing the bundle identifier of the proxy provider to be used by this configuration.

## Relationships

### Inherits From
- [NEVPNProtocol](nevpnprotocol.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class NEDNSProxyManager](nednsproxymanager.md)
  An object to create and manage an DNS proxy provider’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyproviderprotocol)*