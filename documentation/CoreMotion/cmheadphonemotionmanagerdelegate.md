# CMHeadphoneMotionManagerDelegate

**Framework**: Core Motion  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol CMHeadphoneMotionManagerDelegate <NSObject>
```

## Topics

### Connecting and Disconnecting Headphones
- [func headphoneMotionManagerDidConnect(CMHeadphoneMotionManager)](./cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect%28_%29.md)
  Performs a callback to the delegate after you connect headphones.
- [func headphoneMotionManagerDidDisconnect(CMHeadphoneMotionManager)](./cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect%28_%29.md)
  Performs a callback to the delegate after you disconnect headphones.
- [CMHeadphoneMotionManager.DeviceMotionHandler](./cmheadphonemotionmanager/devicemotionhandler.md)
  The type of block callback for handling headphone-motion data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Getting the Delegate
- [var delegate: (any CMHeadphoneMotionManagerDelegate)?](./cmheadphonemotionmanager/delegate.md)
  The object that receives headphone motion manager events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanagerdelegate)*