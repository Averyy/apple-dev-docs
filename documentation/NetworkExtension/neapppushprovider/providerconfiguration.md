# providerConfiguration

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A dictionary that contains current vendor-specific configuration parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var providerConfiguration: [String : Any]? { get }
```

```objc
@property (readonly, nullable) NSDictionary<NSString *,id> * providerConfiguration;
```

## Mentions

- [Maintaining a Reliable Network Connection](../maintaining-a-reliable-network-connection.md)

## Discussion

The [`NEAppPushManager`](../neapppushmanager.md) provides this dictionary. Use key-value observing to watch for changes in the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/providerconfiguration)*