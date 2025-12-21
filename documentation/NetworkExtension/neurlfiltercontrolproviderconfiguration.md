# NEURLFilterControlProviderConfiguration

**Framework**: Network Extension  
**Kind**: class

A class that defines app extension configurations for the URL Filter control provider app extension.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency class NEURLFilterControlProviderConfiguration
```

#### Overview

[`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) uses this class to conform to the [`ExtensionKit`](https://developer.apple.com/documentation/ExtensionKit) framework. Your extension doesn’t need to use this class directly.

## Relationships

### Inherits From
- [NEAppExtensionConfiguration](neappextensionconfiguration.md)
### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
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