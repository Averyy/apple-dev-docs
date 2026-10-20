# NEDNSProxyProviderProtocol

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

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

```objc
@interface NEDNSProxyProviderProtocol : NEVPNProtocol
```

## Topics

### Accessing the DNS proxy configuration
- [var providerConfiguration: [String : Any]?](./nednsproxyproviderprotocol/providerconfiguration.md)
  A dictionary containing vendor-specific configuration parameters for a proxy provider.
- [var providerBundleIdentifier: String?](./nednsproxyproviderprotocol/providerbundleidentifier.md)
  A string containing the bundle identifier of the proxy provider to be used by this configuration.

## Relationships

### Inherits From
- [NEVPNProtocol](./nevpnprotocol.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Configuration
- [class NEDNSProxyManager](./nednsproxymanager.md)
  An object to create and manage an DNS proxy provider’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyproviderprotocol)*