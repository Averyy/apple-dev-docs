# headphoneMotionManagerDidDisconnect(_:)

**Framework**: Core Motion  
**Kind**: method

Performs a callback to the delegate after you disconnect headphones.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- watchOS 7.0+

## Declaration

```swift
optional func headphoneMotionManagerDidDisconnect(_ manager: CMHeadphoneMotionManager)
```

## Parameters

- `manager`: The manager for the disconnected headphones.

## See Also

- [func headphoneMotionManagerDidConnect(CMHeadphoneMotionManager)](cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:).md)
  Performs a callback to the delegate after you connect headphones.
- [CMHeadphoneMotionManager.DeviceMotionHandler](cmheadphonemotionmanager/devicemotionhandler.md)
  The type of block callback for handling headphone-motion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:))*