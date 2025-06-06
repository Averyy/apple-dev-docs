# providerConfiguration

**Framework**: Network Extension  
**Kind**: property

A [`NEFilterProviderConfiguration`](nefilterproviderconfiguration.md) object containing the filter configuration settings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var providerConfiguration: NEFilterProviderConfiguration? { get set }
```

#### Discussion

If this property is nil after calling `loadFromPreferencesWithCompletionHandler:`, then the filter configuration does not exist in the Network Extension preferences.

## See Also

- [var isEnabled: Bool](nefiltermanager/isenabled.md)
  A Boolean used to toggle the enabled state of the filter.
- [var localizedDescription: String?](nefiltermanager/localizeddescription.md)
  A string containing a description of the filter configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/providerconfiguration)*