# quality

**Framework**: RealityKit  
**Kind**: property

The shadow-filtering algorithm this light uses.

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

Set to [`medium`](spotlightcomponent/shadow/qualitymode/medium.md) or [`high`](spotlightcomponent/shadow/qualitymode/high.md) to opt the light into soft shadows, whose penumbra widens with [`lightSize`](spotlightcomponent/shadow/lightsize.md) and with the distance between the caster and the receiving surface. The default value is [`low`](spotlightcomponent/shadow/qualitymode/low.md), which produces a hard-edged shadow whose appearance is independent of [`lightSize`](spotlightcomponent/shadow/lightsize.md).

Higher quality modes use more samples per shadow, which increases GPU work. Excessive use of higher shadow quality lights may contribute to user-noticeable frame drops and can cause the device to heat up in graphically demanding scenes. Monitor the thermal state to lower quality as a mitigation, if necessary. Apps can monitor thermal state changes by subscribing to the [`thermalStateDidChange`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/thermalstatedidchange) notification.

To stay responsive to the device’s available thermal headroom, read `ProcessInfo.processInfo.thermalState` and observe `ProcessInfo.thermalStateDidChangeNotification` to react when it changes. As the reported state moves from `.fair` toward `.serious` and `.critical` switch the light to a lower quality.

## See Also

- [SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode.md)
  Constants that select the shadow-filtering algorithm a spotlight uses.
- [var lightSize: Float](spotlightcomponent/shadow/lightsize.md)
  The radius of the spotlight’s emitting surface, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/quality)*