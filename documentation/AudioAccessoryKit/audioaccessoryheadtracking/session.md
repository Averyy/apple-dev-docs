# AudioAccessoryHeadTracking.Session

**Framework**: AudioAccessoryKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)

## Declaration

```swift
final class Session
```

## Topics

### Instance Properties
- [var isHeadTrackingActive: Bool](audioaccessoryheadtracking/session/isheadtrackingactive.md)
  Returns `true` when head tracking is currently enabled for this accessory; `false` otherwise.
- [let restorationID: String?](audioaccessoryheadtracking/session/restorationid.md)
  A stable identifier the system uses to bring this extension out of suspension when sensor traffic arrives for this accessory.
### Instance Methods
- [func sendDataToAudioExtension(Data) throws](audioaccessoryheadtracking/session/senddatatoaudioextension(_:).md)
  Forward a frame of IMU sensor data from the accessory to the Spatial Audio renderer.

## Relationships

### Conforms To
- [AccessoryFeatureSession](../accessorytransportextension/accessoryfeaturesession.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/session)*