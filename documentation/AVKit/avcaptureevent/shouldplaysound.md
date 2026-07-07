# shouldPlaySound

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether you must play a sound manually.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var shouldPlaySound: Bool { get }
```

#### Discussion

This property is `true` only when both of the following conditions are true:

1. A person performs an AirPod stem click.
2. You disable the default capture sound.

If this property is `false`, calling [`play(_:)`](avcaptureevent/play(_:).md) has no effect. Omitting the sound when expected can significantly impact the user experience.

> ❗ **Important**: To use AirPods Camera Control, it must be available in your country or region. AirPods Camera Control is not currently available in the European Union.

## See Also

- [func play(AVCaptureEventSound) -> Bool](avcaptureevent/play(_:).md)
  Plays the specified capture sound through AirPods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureevent/shouldplaysound)*