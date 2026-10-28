# NEDNSProxyManagerError

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NEDNSProxyManagerError : NSInteger;
```

## Overview

These errors appear as the parameter in the completion handler of the methods that you use to manage DNS proxy configuration: [`loadFromPreferences(completionHandler:)`](./nednsproxymanager/loadfrompreferences%28completionhandler%29.md), [`removeFromPreferences(completionHandler:)`](./nednsproxymanager/removefrompreferences%28completionhandler%29.md), and [`saveToPreferences(completionHandler:)`](./nednsproxymanager/savetopreferences%28completionhandler%29.md).

## Topics

### Enumeration Cases
- [NEDNSProxyManagerError.configurationInvalid](./nednsproxymanagererror/configurationinvalid.md)
  Invalid DNS proxy configuration that cannot be stored.
- [NEDNSProxyManagerError.configurationDisabled](./nednsproxymanagererror/configurationdisabled.md)
  Disabled DNS proxy configuration.
- [NEDNSProxyManagerError.configurationStale](./nednsproxymanagererror/configurationstale.md)
  Outdated DNS proxy configuration that needs to be loaded.
- [NEDNSProxyManagerError.configurationCannotBeRemoved](./nednsproxymanagererror/configurationcannotberemoved.md)
  Unremovable DNS proxy configuration.
### Initializers
- [init?(rawValue: Int)](./nednsproxymanagererror/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [let NEDNSProxyErrorDomain: String](./nednsproxyerrordomain.md)
  The DNS proxy error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanagererror)*