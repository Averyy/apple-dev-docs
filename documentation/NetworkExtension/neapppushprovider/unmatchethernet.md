# unmatchEthernet()

**Framework**: Network Extension  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
func unmatchEthernet()
```

#### Discussion

This method is called by the provider when it does not require runtime while the device is connected to the current Ethernet network. This method is applicable only when NEAppPushManager has set matchEthernet property to YES and the provider is running because the device is connected to an Ethernet network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider/unmatchethernet())*