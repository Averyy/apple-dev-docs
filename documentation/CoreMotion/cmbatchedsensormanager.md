# CMBatchedSensorManager

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class CMBatchedSensorManager
```

```objc
@interface CMBatchedSensorManager : NSObject
```

## Mentions

- [Getting processed device-motion data](./getting-processed-device-motion-data.md)

## Topics

### Determining authorization and availability
- [class var authorizationStatus: CMAuthorizationStatus](./cmbatchedsensormanager/authorizationstatus.md)
- [class var isAccelerometerSupported: Bool](./cmbatchedsensormanager/isaccelerometersupported.md)
- [class var isDeviceMotionSupported: Bool](./cmbatchedsensormanager/isdevicemotionsupported.md)
### Configuring the update frequency
- [var deviceMotionDataFrequency: Int](./cmbatchedsensormanager/devicemotiondatafrequency.md)
- [var accelerometerDataFrequency: Int](./cmbatchedsensormanager/accelerometerdatafrequency.md)
### Collecting device-motion data
- [func startDeviceMotionUpdates()](./cmbatchedsensormanager/startdevicemotionupdates%28%29.md)
- [func startDeviceMotionUpdates(handler: ([CMDeviceMotion]?, (any Error)?) -> Void)](./cmbatchedsensormanager/startdevicemotionupdates%28handler%29.md)
- [func stopDeviceMotionUpdates()](./cmbatchedsensormanager/stopdevicemotionupdates%28%29.md)
- [var deviceMotionBatch: [CMDeviceMotion]?](./cmbatchedsensormanager/devicemotionbatch.md)
- [func deviceMotionUpdates() -> CMBatchedSensorManager.DeviceMotionUpdates](./cmbatchedsensormanager/devicemotionupdates%28%29.md)
- [CMBatchedSensorManager.DeviceMotionUpdates](./cmbatchedsensormanager/devicemotionupdates.md)
- [var isDeviceMotionActive: Bool](./cmbatchedsensormanager/isdevicemotionactive.md)
### Collecting accelerometer data
- [func startAccelerometerUpdates()](./cmbatchedsensormanager/startaccelerometerupdates%28%29.md)
- [func startAccelerometerUpdates(handler: ([CMAccelerometerData]?, (any Error)?) -> Void)](./cmbatchedsensormanager/startaccelerometerupdates%28handler%29.md)
- [func stopAccelerometerUpdates()](./cmbatchedsensormanager/stopaccelerometerupdates%28%29.md)
- [var accelerometerBatch: [CMAccelerometerData]?](./cmbatchedsensormanager/accelerometerbatch.md)
- [func accelerometerUpdates() -> CMBatchedSensorManager.AccelerometerUpdates](./cmbatchedsensormanager/accelerometerupdates%28%29.md)
- [CMBatchedSensorManager.AccelerometerUpdates](./cmbatchedsensormanager/accelerometerupdates.md)
- [var isAccelerometerActive: Bool](./cmbatchedsensormanager/isaccelerometeractive.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)*