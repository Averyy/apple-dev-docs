# CMHeadphoneMotionManager.DeviceMotionHandler

**Framework**: Core Motion  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(CMDeviceMotion *, NSError *) CMHeadphoneDeviceMotionHandler;
```

#### Discussion

The system calls `CMDeviceMotionHandler` blocks when there is device-motion data to process. You pass the block into [`startDeviceMotionUpdates(to:withHandler:)`](./startdevicemotionupdates%28to,withhandler%29.md) as the second argument. Blocks of this type return no value, but take two arguments:

- **`motion`**: A [`CMHeadphoneMotionManager`](../cmheadphonemotionmanager.md) object, which encapsulates other objects and a structure representing attitude, rotation rate, gravity, and user acceleration.
- **`error`**: An error object representing an error when providing gyroscope data. If an error occurs, you should stop gyroscope updates and inform the user of the problem. If there is no error, this argument is `nil`. Core Motion errors are of the [`CMErrorDomain`](../cmerrordomain.md) domain and the [`CMError`](../cmerror.md) type.

## See Also

### Connecting and Disconnecting Headphones
- [func headphoneMotionManagerDidConnect(CMHeadphoneMotionManager)](../cmheadphonemotionmanagerdelegate/headphonemotionmanagerdidconnect%28_%29.md)
  Performs a callback to the delegate after you connect headphones.
- [func headphoneMotionManagerDidDisconnect(CMHeadphoneMotionManager)](../cmheadphonemotionmanagerdelegate/headphonemotionmanagerdiddisconnect%28_%29.md)
  Performs a callback to the delegate after you disconnect headphones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/devicemotionhandler)*