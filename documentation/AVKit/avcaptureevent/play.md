# play(_:)

**Framework**: AVKit  
**Kind**: method

Plays the specified capture sound through AirPods.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func play(_ sound: AVCaptureEventSound) -> Bool
```

#### Return Value

A Boolean value that indicates whether the system played the sound.

#### Discussion

This method has no effect if [`shouldPlaySound`](avcaptureevent/shouldplaysound.md) is `false` or if the event object’s lifetime exceeds 15 seconds.

> ❗ **Important**: To use AirPods Camera Control, it must be available in your country or region. AirPods Camera Control is not currently available in the European Union.

## Parameters

- `sound`: The capture sound to play for this event.

## See Also

- [var shouldPlaySound: Bool](avcaptureevent/shouldplaysound.md)
  A Boolean value that indicates whether you must play a sound manually.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureevent/play(_:))*