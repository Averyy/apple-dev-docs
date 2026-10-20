# AudioAccessoryHeadTracking.Session

**Framework**: AudioAccessoryKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+

## Declaration

```swift
final class Session
```

## Topics

### Instance Properties
- [var isHeadTrackingActive: Bool](./session/isheadtrackingactive.md)
  Returns `true` when head tracking is currently enabled for this accessory; `false` otherwise.
- [let restorationID: String?](./session/restorationid.md)
  A stable identifier the system uses to bring this extension out of suspension when sensor traffic arrives for this accessory.
### Instance Methods
- [func sendDataToAudioExtension(Data) throws](./session/senddatatoaudioextension%28_%29.md)
  Forward a frame of IMU sensor data from the accessory to the Spatial Audio renderer.

## Relationships

### Conforms To
- [AccessoryFeatureSession](../../AccessoryTransportExtension/accessoryfeaturesession.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/session)*