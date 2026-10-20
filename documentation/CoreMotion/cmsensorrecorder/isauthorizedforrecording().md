# isAuthorizedForRecording()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value indicating whether the app is authorized to record sensor data.

**Availability**:
- iOS 9.0+ - Deprecated in 11.0
- iPadOS 9.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use [`authorizationStatus()`](./authorizationstatus%28%29.md) instead.

## Declaration

```swift
class func isAuthorizedForRecording() -> Bool
```

```objc
+ (BOOL) isAuthorizedForRecording;
```

#### Return Value

[`true`](../../Swift/true.md) if the app is authorized to record sensor data or [`false`](../../Swift/false.md) if it is not.

## See Also

### Checking the Availability of Sensor Recording
- [class func isAccelerometerRecordingAvailable() -> Bool](./isaccelerometerrecordingavailable%28%29.md)
  Returns a Boolean value indicating whether accelerometer recording is supported on the current device.
- [class func authorizationStatus() -> CMAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns a value indicating whether the app is authorized to record sensor data.
- [enum CMAuthorizationStatus](../cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isauthorizedforrecording())*