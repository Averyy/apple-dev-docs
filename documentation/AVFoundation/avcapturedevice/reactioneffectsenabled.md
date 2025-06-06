# reactionEffectsEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the app supports performing reaction effects.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class var reactionEffectsEnabled: Bool { get }
```

#### Discussion

The system only renders reaction effects when the device’s active format supports the feature, which you determine by querying the value of its [`reactionEffectsSupported`](avcapturedevice/format/reactioneffectssupported.md) property.

In macOS, the system enables reaction effects for all apps by default. In iOS, it enables them by default only for video conferencing apps (apps that enable the Voice over IP option in their [`UIBackgroundModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIBackgroundModes) configuration). Apps that don’t use this background mode may opt in to this feature by adding the following key to the `Info.plist` file.

```swift
<key>NSCameraReactionEffectsEnabled</key>
<true/>
```

## See Also

- [var canPerformReactionEffects: Bool](avcapturedevice/canperformreactioneffects.md)
  A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [var availableReactionTypes: Set<AVCaptureReactionType>](avcapturedevice/availablereactiontypes.md)
  A set of reactions types that a device supports performing.
- [class var reactionEffectGesturesEnabled: Bool](avcapturedevice/reactioneffectgesturesenabled.md)
  A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [func performEffect(for: AVCaptureReactionType)](avcapturedevice/performeffect(for:).md)
  Performs the specified reaction type on the video stream.
- [var reactionEffectsInProgress: [AVCaptureReactionEffectState]](avcapturedevice/reactioneffectsinprogress.md)
  An array of reaction effects that the device is currently performing, sorted by timestamp.
- [class AVCaptureReactionEffectState](avcapturereactioneffectstate.md)
  An object that reports the state of a reaction effect performed on a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/reactioneffectsenabled)*