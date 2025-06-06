# NEDNSProxyManagerError.configurationCannotBeRemoved

**Framework**: Network Extension  
**Kind**: case

Unremovable DNS proxy configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case configurationCannotBeRemoved
```

#### Discussion

This error occurs if you attempt to use a call to the [`removeFromPreferences(completionHandler:)`](nednsproxymanager/removefrompreferences(completionhandler:).md) method to remove the DNS proxy configuration when an installed configuration profile specifies a baseline DNS proxy configuration. You can only call the removal method in a development environment where no configuration profile exists.

## See Also

- [NEDNSProxyManagerError.configurationInvalid](nednsproxymanagererror/configurationinvalid.md)
  Invalid DNS proxy configuration that cannot be stored.
- [NEDNSProxyManagerError.configurationDisabled](nednsproxymanagererror/configurationdisabled.md)
  Disabled DNS proxy configuration.
- [NEDNSProxyManagerError.configurationStale](nednsproxymanagererror/configurationstale.md)
  Outdated DNS proxy configuration that needs to be loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanagererror/configurationcannotberemoved)*