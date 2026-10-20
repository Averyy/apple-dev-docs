# quality

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The shadow-filtering algorithm this light uses.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS
- visionOS 27.0+

## Declaration

```swift
var quality: SpotLightComponent.Shadow.QualityMode { get set }
```

#### Discussion

Set to [`medium`](./qualitymode/medium.md) or [`high`](./qualitymode/high.md) to opt the light into soft shadows, whose penumbra widens with [`lightSize`](./lightsize.md) and with the distance between the caster and the receiving surface. The default value is [`low`](./qualitymode/low.md), which produces a hard-edged shadow whose appearance is independent of [`lightSize`](./lightsize.md).

Higher quality modes use more samples per shadow, which increases GPU work. Excessive use of higher shadow quality lights may contribute to user-noticeable frame drops and can cause the device to heat up in graphically demanding scenes. Monitor the thermal state to lower quality as a mitigation, if necessary. Apps can monitor thermal state changes by subscribing to the [thermalStateDidChange](../../../Foundation/notificationcenter/messageidentifier/thermalstatedidchange.md) notification.

To stay responsive to the device’s available thermal headroom, read `ProcessInfo.processInfo.thermalState` and observe `ProcessInfo.thermalStateDidChangeNotification` to react when it changes. As the reported state moves from `.fair` toward `.serious` and `.critical` switch the light to a lower quality.

## See Also

### Configuring shadow quality
- [SpotLightComponent.Shadow.QualityMode](./qualitymode.md)
  Constants that select the shadow-filtering algorithm a spotlight uses.
- [var lightSize: Float](./lightsize.md)
  The radius of the spotlight’s emitting surface, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/quality)*