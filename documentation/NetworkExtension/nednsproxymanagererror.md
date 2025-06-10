# NEDNSProxyManagerError

**Framework**: Network Extension  
**Kind**: enum

The possible DNS proxy manager errors.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum NEDNSProxyManagerError
```

#### Overview

These errors appear as the parameter in the completion handler of the methods that you use to manage DNS proxy configuration: [`loadFromPreferences(completionHandler:)`](nednsproxymanager/loadfrompreferences(completionhandler:).md), [`removeFromPreferences(completionHandler:)`](nednsproxymanager/removefrompreferences(completionhandler:).md), and [`saveToPreferences(completionHandler:)`](nednsproxymanager/savetopreferences(completionhandler:).md).

## Topics

### Enumeration Cases
- [NEDNSProxyManagerError.configurationInvalid](nednsproxymanagererror/configurationinvalid.md)
  Invalid DNS proxy configuration that cannot be stored.
- [NEDNSProxyManagerError.configurationDisabled](nednsproxymanagererror/configurationdisabled.md)
  Disabled DNS proxy configuration.
- [NEDNSProxyManagerError.configurationStale](nednsproxymanagererror/configurationstale.md)
  Outdated DNS proxy configuration that needs to be loaded.
- [NEDNSProxyManagerError.configurationCannotBeRemoved](nednsproxymanagererror/configurationcannotberemoved.md)
  Unremovable DNS proxy configuration.
### Initializers
- [init?(rawValue: Int)](nednsproxymanagererror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let NEDNSProxyErrorDomain: String](nednsproxyerrordomain.md)
  The DNS proxy error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanagererror)*