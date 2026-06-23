# quality

**Framework**: RealityKit  
**Kind**: property

The quality of the soft shadows this light casts.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS 27.0+ (Beta)

## Declaration

```swift
var quality: SpotLightComponent.Shadow.QualityMode { get set }
```

#### Discussion

Higher quality modes use more samples per shadow, which increases GPU work. Excessive use of higher shadow quality lights may contribute to user-noticeable frame drops and can cause the device to heat up in graphically demanding scenes. Monitor the thermal state to lower quality as a mitigation, if necessary. Apps can monitor thermal state changes by subscribing to the [`thermalStateDidChange`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/thermalstatedidchange) notification.

To stay responsive to the device’s available thermal headroom, read `ProcessInfo.processInfo.thermalState` and observe `ProcessInfo.thermalStateDidChangeNotification` to react when it changes. As the reported state moves from `.fair` toward `.serious` and `.critical` switch the light to a lower quality.

## See Also

- [SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode.md)
  The quality for the shadows. Low uses shadows that don’t change with light size and the distance between light-blocker-receiver Medium and high allow soft shadows with varying sample counts
- [var lightSize: Float](spotlightcomponent/shadow/lightsize.md)
  The light size that determines the softness of the shadows Larger size would mean a larger penumbra and a larger transition range from fully shadowed to lit. It is the radius of the light in world space units. It is also modulated by the attenaution radius, i.e., lights with larger attenuation radius need larger light size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/quality)*