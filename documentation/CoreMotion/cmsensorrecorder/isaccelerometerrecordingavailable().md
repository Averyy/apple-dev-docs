# isAccelerometerRecordingAvailable()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value indicating whether accelerometer recording is supported on the current device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class func isAccelerometerRecordingAvailable() -> Bool
```

```objc
+ (BOOL) isAccelerometerRecordingAvailable;
```

#### Return Value

[`true`](../../Swift/true.md) if accelerometer recording is available or [`false`](../../Swift/false.md) if it is not.

#### Discussion

Call this method before trying to record or retrieve any accelerometer data using the methods of this class. Accelerometer data recording is not supported on all devices.

## See Also

### Checking the Availability of Sensor Recording
- [class func authorizationStatus() -> CMAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns a value indicating whether the app is authorized to record sensor data.
- [enum CMAuthorizationStatus](../cmauthorizationstatus.md)
  The authorization status for motion-related features.
- [class func isAuthorizedForRecording() -> Bool](./isauthorizedforrecording%28%29.md)
  Returns a Boolean value indicating whether the app is authorized to record sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isaccelerometerrecordingavailable())*