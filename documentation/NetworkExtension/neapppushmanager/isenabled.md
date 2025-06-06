# isEnabled

**Framework**: Network Extension  
**Kind**: property

A property you use to toggle enabling the configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

The framework sets this value to NO when your app saves a configuration that overlaps with this configuration. This overlap occurs when a new [`NEAppPushManager`](neapppushmanager.md) saves a configuration with a [`matchSSIDs`](neapppushmanager/matchssids.md) list that contains an SSID which is also a member of this manager’s SSID list.

## See Also

- [var isActive: Bool](neapppushmanager/isactive.md)
  A Boolean value that indicates whether a configuration is in use.
- [var localizedDescription: String?](neapppushmanager/localizeddescription.md)
  A string that contains the localized description of the app push manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/isenabled)*