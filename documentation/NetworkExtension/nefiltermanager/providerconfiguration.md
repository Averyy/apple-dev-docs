# providerConfiguration

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A [`NEFilterProviderConfiguration`](../nefilterproviderconfiguration.md) object containing the filter configuration settings.

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

```objc
@property (strong, nullable) NEFilterProviderConfiguration * providerConfiguration;
```

#### Discussion

If this property is nil after calling `loadFromPreferencesWithCompletionHandler:`, then the filter configuration does not exist in the Network Extension preferences.

## See Also

### Accessing filter configuration properties
- [var isEnabled: Bool](./isenabled.md)
  A Boolean used to toggle the enabled state of the filter.
- [var localizedDescription: String?](./localizeddescription.md)
  A string containing a description of the filter configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/providerconfiguration)*