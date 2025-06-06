# CMBatchedSensorManager

**Framework**: Core Motion  
**Kind**: class

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

## Mentions

- [Getting processed device-motion data](getting-processed-device-motion-data.md)

## Topics

### Determining authorization and availability
- [class var authorizationStatus: CMAuthorizationStatus](cmbatchedsensormanager/authorizationstatus.md)
- [class var isAccelerometerSupported: Bool](cmbatchedsensormanager/isaccelerometersupported.md)
- [class var isDeviceMotionSupported: Bool](cmbatchedsensormanager/isdevicemotionsupported.md)
### Configuring the update frequency
- [var deviceMotionDataFrequency: Int](cmbatchedsensormanager/devicemotiondatafrequency.md)
- [var accelerometerDataFrequency: Int](cmbatchedsensormanager/accelerometerdatafrequency.md)
### Collecting device-motion data
- [func startDeviceMotionUpdates()](cmbatchedsensormanager/startdevicemotionupdates.md)
- [func startDeviceMotionUpdates(handler: ([CMDeviceMotion]?, (any Error)?) -> Void)](cmbatchedsensormanager/startdevicemotionupdates(handler:).md)
- [func stopDeviceMotionUpdates()](cmbatchedsensormanager/stopdevicemotionupdates.md)
- [var deviceMotionBatch: [CMDeviceMotion]?](cmbatchedsensormanager/devicemotionbatch.md)
- [func deviceMotionUpdates() -> CMBatchedSensorManager.DeviceMotionUpdates](cmbatchedsensormanager/devicemotionupdates.md)
- [CMBatchedSensorManager.DeviceMotionUpdates](cmbatchedsensormanager/devicemotionupdates.md)
- [var isDeviceMotionActive: Bool](cmbatchedsensormanager/isdevicemotionactive.md)
### Collecting accelerometer data
- [func startAccelerometerUpdates()](cmbatchedsensormanager/startaccelerometerupdates.md)
- [func startAccelerometerUpdates(handler: ([CMAccelerometerData]?, (any Error)?) -> Void)](cmbatchedsensormanager/startaccelerometerupdates(handler:).md)
- [func stopAccelerometerUpdates()](cmbatchedsensormanager/stopaccelerometerupdates.md)
- [var accelerometerBatch: [CMAccelerometerData]?](cmbatchedsensormanager/accelerometerbatch.md)
- [func accelerometerUpdates() -> CMBatchedSensorManager.AccelerometerUpdates](cmbatchedsensormanager/accelerometerupdates.md)
- [CMBatchedSensorManager.AccelerometerUpdates](cmbatchedsensormanager/accelerometerupdates.md)
- [var isAccelerometerActive: Bool](cmbatchedsensormanager/isaccelerometeractive.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)*