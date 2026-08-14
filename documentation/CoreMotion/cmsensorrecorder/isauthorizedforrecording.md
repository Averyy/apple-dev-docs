# isAuthorizedForRecording()

**Framework**: Core Motion  
**Kind**: method

Returns a Boolean value indicating whether the app is authorized to record sensor data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class func isAuthorizedForRecording() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the app is authorized to record sensor data or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

## See Also

- [class func isAccelerometerRecordingAvailable() -> Bool](cmsensorrecorder/isaccelerometerrecordingavailable.md)
  Returns a Boolean value indicating whether accelerometer recording is supported on the current device.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmsensorrecorder/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to record sensor data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/isauthorizedforrecording())*