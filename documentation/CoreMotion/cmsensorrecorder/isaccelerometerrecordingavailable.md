# isAccelerometerRecordingAvailable()

**Framework**: Core Motion  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if accelerometer recording is available or [`false`](https://developer.apple.com/documentation/Swift/false) if it is not.

#### Discussion

Call this method before trying to record or retrieve any accelerometer data using the methods of this class. Accelerometer data recording is not supported on all devices.

## See Also

- [class func authorizationStatus() -> CMAuthorizationStatus](cmsensorrecorder/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to record sensor data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.
- [class func isAuthorizedForRecording() -> Bool](cmsensorrecorder/isauthorizedforrecording.md)
  Returns a Boolean value indicating whether the app is authorized to record sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isaccelerometerrecordingavailable())*