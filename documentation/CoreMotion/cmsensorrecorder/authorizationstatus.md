# authorizationStatus()

**Framework**: Core Motion  
**Kind**: method

Returns a value indicating whether the app is authorized to record sensor data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- watchOS 4.0+

## Declaration

```swift
class func authorizationStatus() -> CMAuthorizationStatus
```

## See Also

- [class func isAccelerometerRecordingAvailable() -> Bool](cmsensorrecorder/isaccelerometerrecordingavailable.md)
  Returns a Boolean value indicating whether accelerometer recording is supported on the current device.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.
- [class func isAuthorizedForRecording() -> Bool](cmsensorrecorder/isauthorizedforrecording.md)
  Returns a Boolean value indicating whether the app is authorized to record sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/authorizationstatus())*