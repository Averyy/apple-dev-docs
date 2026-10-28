# providerConfiguration

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy) NSDictionary<NSString *,id> * providerConfiguration;
```

## Discussion

The dictionary’s values must only use data types supported by [`PropertyListSerialization`](../../Foundation/propertylistserialization.md); you can’t use custom types for the values.

The manager passes this dictionary as-is to the [`NEAppPushProvider`](../neapppushprovider.md) when the provider starts.

## See Also

### Inspecting provider properties
- [var providerBundleIdentifier: String?](./providerbundleidentifier.md)
  A string that contains the bundle identifier of the push provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/providerconfiguration)*