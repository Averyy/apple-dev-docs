# unmatchEthernet()

**Framework**: Network Extension  
**Kind**: method

Tells the framework not to use the provider with an active Ethernet connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func unmatchEthernet()
```

#### Discussion

Call this method when the provider doesn’t need to operate if the device’s active network connection is Ethernet. Typically, you call this if you determine the provider isn’t compatible with the network when running over Ethernet.

This method is only applicable when all of the following are true:

- The [`NEAppPushManager`](neapppushmanager.md) property [`matchEthernet`](neapppushmanager/matchethernet.md) is `true` (Swift) or `YES` (Objective-C).
- The iOS device is connected to an Ethernet network.
- The Ethernet network is the primary route on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/unmatchethernet())*