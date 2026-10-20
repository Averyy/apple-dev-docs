# NEDNSProxyManagerError.configurationStale

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

Outdated DNS proxy configuration that needs to be loaded.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case configurationStale
```

```c
NEDNSProxyManagerErrorConfigurationStale
```

#### Discussion

You must load the configuration with a call to [`loadFromPreferences(completionHandler:)`](../nednsproxymanager/loadfrompreferences%28completionhandler%29.md) before you can save it.

## See Also

### Enumeration Cases
- [NEDNSProxyManagerError.configurationInvalid](./configurationinvalid.md)
  Invalid DNS proxy configuration that cannot be stored.
- [NEDNSProxyManagerError.configurationDisabled](./configurationdisabled.md)
  Disabled DNS proxy configuration.
- [NEDNSProxyManagerError.configurationCannotBeRemoved](./configurationcannotberemoved.md)
  Unremovable DNS proxy configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanagererror/configurationstale)*