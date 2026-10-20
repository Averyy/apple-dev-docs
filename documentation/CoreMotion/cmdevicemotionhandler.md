# CMDeviceMotionHandler

**Framework**: Core Motion  
**Kind**: typealias  
**Role**: Type Alias

The type of block callback for handling device-motion data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias CMDeviceMotionHandler = (CMDeviceMotion?, (any Error)?) -> Void
```

```c
typedef void (^)(CMDeviceMotion *, NSError *) CMDeviceMotionHandler;
```

## Mentions

- [Getting processed device-motion data](./getting-processed-device-motion-data.md)

#### Discussion

Blocks of type `CMDeviceMotionHandler` are called when there is device-motion data to process. You pass the block into [`startDeviceMotionUpdates(to:withHandler:)`](./cmmotionmanager/startdevicemotionupdates%28to,withhandler%29.md) as the second argument. Blocks of this type return no value but take two arguments:

- **`motion`**: A [`CMDeviceMotion`](./cmdevicemotion.md) object, which encapsulates other objects and a structure representing attitude, rotation rate, gravity, and user acceleration.
- **`error`**: An error object representing an error encountered in providing device-motion data. If an error occurs, you should stop device-motion data updates and inform the user of the problem. If there is no error, this argument is `nil`. Core Motion errors are of the [`CMErrorDomain`](./cmerrordomain.md) domain and the [`CMError`](./cmerror.md) type.

## See Also

### Managing device motion updates
- [var deviceMotionBody: (any CMBodyIdentifiable)?](./cmmotionmanager/devicemotionbody.md)
  A physical body or view that defines the coordinate system for device-motion data.
- [var showsDeviceMovementDisplay: Bool](./cmmotionmanager/showsdevicemovementdisplay.md)
  Controls whether the device-movement display is shown.
- [var deviceMotionUpdateInterval: TimeInterval](./cmmotionmanager/devicemotionupdateinterval.md)
  The interval, in seconds, for providing device-motion updates to the block handler.
- [func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)](./cmmotionmanager/startdevicemotionupdates%28using,to,withhandler%29.md)
  Starts device-motion updates on an operation queue and using a specified reference frame and block handler.
- [func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)](./cmmotionmanager/startdevicemotionupdates%28to,withhandler%29.md)
  Starts device-motion updates on an operation queue and using a specified block handler.
- [func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)](./cmmotionmanager/startdevicemotionupdates%28using%29.md)
  Starts device-motion updates using a reference frame but without a block handler.
- [func startDeviceMotionUpdates()](./cmmotionmanager/startdevicemotionupdates%28%29.md)
  Starts device-motion updates without a block handler.
- [func stopDeviceMotionUpdates()](./cmmotionmanager/stopdevicemotionupdates%28%29.md)
  Stops device-motion updates.
- [var deviceMotion: CMDeviceMotion?](./cmmotionmanager/devicemotion.md)
  The latest sample of device-motion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)*