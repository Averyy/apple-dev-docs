# shared

**Framework**: Network Extension  
**Kind**: property

Instantiates [`NEHotspotConfigurationManager`](nehotspotconfigurationmanager.md) as a singleton, so it can be shared.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class var shared: NEHotspotConfigurationManager { get }
```

## See Also

- [func apply(NEHotspotConfiguration, completionHandler: (((any Error)?) -> Void)?)](nehotspotconfigurationmanager/apply(_:completionhandler:).md)
  Adds or updates a Wi-Fi network configuration after prompting the user for permission, and then attempts to join the network under certain conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfigurationmanager/shared)*