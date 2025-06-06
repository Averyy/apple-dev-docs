# CMHeadphoneMotionManager.DeviceMotionHandler

**Framework**: Core Motion  
**Kind**: typealias

The type of block callback for handling headphone-motion data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
typealias DeviceMotionHandler = (CMDeviceMotion?, (any Error)?) -> Void
```

#### Discussion

The system calls `CMDeviceMotionHandler` blocks when there is device-motion data to process. You pass the block into [`startDeviceMotionUpdates(to:withHandler:)`](cmheadphonemotionmanager/startdevicemotionupdates(to:withhandler:).md) as the second argument. Blocks of this type return no value, but take two arguments:

## See Also

- [func headphoneMotionManagerDidConnect(CMHeadphoneMotionManager)](cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:).md)
  Performs a callback to the delegate after you connect headphones.
- [func headphoneMotionManagerDidDisconnect(CMHeadphoneMotionManager)](cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:).md)
  Performs a callback to the delegate after you disconnect headphones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotionhandler)*