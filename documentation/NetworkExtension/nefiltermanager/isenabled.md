# isEnabled

**Framework**: Network Extension  
**Kind**: property

A Boolean used to toggle the enabled state of the filter.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) and saving the configuration will disable all other network content filters on the system, and will start the filter’s Filter Provider extensions. Setting this property to false and saving the configuration will disable the filter and stop the filter’s Filter Provider extensions.

## See Also

- [var providerConfiguration: NEFilterProviderConfiguration?](nefiltermanager/providerconfiguration.md)
  A [`NEFilterProviderConfiguration`](nefilterproviderconfiguration.md) object containing the filter configuration settings.
- [var localizedDescription: String?](nefiltermanager/localizeddescription.md)
  A string containing a description of the filter configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/isenabled)*