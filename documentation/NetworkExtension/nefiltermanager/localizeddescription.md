# localizedDescription

**Framework**: Network Extension  
**Kind**: property

A string containing a description of the filter configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var localizedDescription: String? { get set }
```

#### Discussion

If this property is set to nil at the time that the configuration is created, it will be automatically set to the display name of the calling app.

## See Also

- [var isEnabled: Bool](nefiltermanager/isenabled.md)
  A Boolean used to toggle the enabled state of the filter.
- [var providerConfiguration: NEFilterProviderConfiguration?](nefiltermanager/providerconfiguration.md)
  A [`NEFilterProviderConfiguration`](nefilterproviderconfiguration.md) object containing the filter configuration settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/localizeddescription)*