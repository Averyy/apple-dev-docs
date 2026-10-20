# isEnabled

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (getter=isEnabled) BOOL enabled;
```

#### Discussion

Setting this property to [`true`](../../Swift/true.md) and saving the configuration will disable all other network content filters on the system, and will start the filter’s Filter Provider extensions. Setting this property to false and saving the configuration will disable the filter and stop the filter’s Filter Provider extensions.

## See Also

### Accessing filter configuration properties
- [var providerConfiguration: NEFilterProviderConfiguration?](./providerconfiguration.md)
  A [`NEFilterProviderConfiguration`](../nefilterproviderconfiguration.md) object containing the filter configuration settings.
- [var localizedDescription: String?](./localizeddescription.md)
  A string containing a description of the filter configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/isenabled)*