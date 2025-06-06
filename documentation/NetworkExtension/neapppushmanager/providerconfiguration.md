# providerConfiguration

**Framework**: Network Extension  
**Kind**: property

A dictionary that contains vendor-specific key-value pairs, that you use to configure a provider.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var providerConfiguration: [String : Any] { get set }
```

#### Discussion

The dictionary’s values must only use data types supported by [`PropertyListSerialization`](https://developer.apple.com/documentation/Foundation/PropertyListSerialization); you can’t use custom types for the values.

The manager passes this dictionary as-is to the [`NEAppPushProvider`](neapppushprovider.md) when the provider starts.

## See Also

- [var providerBundleIdentifier: String?](neapppushmanager/providerbundleidentifier.md)
  A string that contains the bundle identifier of the push provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/providerconfiguration)*