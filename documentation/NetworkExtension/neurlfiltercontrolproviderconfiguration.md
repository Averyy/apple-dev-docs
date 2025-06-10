# NEURLFilterControlProviderConfiguration

**Framework**: Network Extension  
**Kind**: class

A class that defines app extension configurations for the URL Filter control provider app extension.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency class NEURLFilterControlProviderConfiguration
```

#### Overview

[`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) uses this class to conform to the [`ExtensionKit`](https://developer.apple.com/documentation/ExtensionKit) framework. Your extension doesn’t need to use this class directly.

## Topics

### Creating a provider configuration
- [init(appex: any NEURLFilterControlProvider)](neurlfiltercontrolproviderconfiguration/init(appex:).md)
  Creates a configuration for a given app extension.

## Relationships

### Inherits From
- [NEAppExtensionConfiguration](neappextensionconfiguration.md)
### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [NEAppExtensionConfigurationProtocol](neappextensionconfigurationprotocol.md)
- [NEAppExtensionXPCProtocol](neappextensionxpcprotocol.md)
- [NEURLFilterControlProviderXPCProtocol](neurlfiltercontrolproviderxpcprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NEURLFilterManager](neurlfiltermanager.md)
  A class you use to configure and control a URL filter.
- [protocol NEURLFilterControlProvider](neurlfiltercontrolprovider.md)
  A protocol that defines an object that’s responsible for fetching pre-filter data.
- [class NEURLFilter](neurlfilter.md)
  A class used to voluntarily validate URLs for apps that don’t use WebKit or the URL session API.
- [Filtering traffic by URL](filtering-traffic-by-url.md)
  Perform fast and robust filtering of full URLs by managing URL filtering configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltercontrolproviderconfiguration)*