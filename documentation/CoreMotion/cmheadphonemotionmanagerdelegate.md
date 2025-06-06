# CMHeadphoneMotionManagerDelegate

**Framework**: Core Motion  
**Kind**: protocol

A set of methods that defines an interface for connecting and disconnecting headphones.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- watchOS 7.0+

## Declaration

```swift
protocol CMHeadphoneMotionManagerDelegate : NSObjectProtocol
```

## Topics

### Connecting and Disconnecting Headphones
- [func headphoneMotionManagerDidConnect(CMHeadphoneMotionManager)](cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect(_:).md)
  Performs a callback to the delegate after you connect headphones.
- [func headphoneMotionManagerDidDisconnect(CMHeadphoneMotionManager)](cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect(_:).md)
  Performs a callback to the delegate after you disconnect headphones.
- [CMHeadphoneMotionManager.DeviceMotionHandler](cmheadphonemotionmanager/devicemotionhandler.md)
  The type of block callback for handling headphone-motion data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any CMHeadphoneMotionManagerDelegate)?](cmheadphonemotionmanager/delegate.md)
  The object that receives headphone motion manager events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate)*