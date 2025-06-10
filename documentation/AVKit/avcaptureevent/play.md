# play(_:)

**Framework**: AVKit  
**Kind**: method

Plays the given capture sound through AirPods.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func play(_ sound: AVCaptureEventSound) -> Bool
```

#### Return Value

A BOOL indicating whether a sound was played or not.

#### Discussion

This method has no effect if `shouldPlaySound` is `NO` or if the event object’s lifetime exceeds 15 seconds.

## Parameters

- `sound`: The capture sound to play for this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureevent/play(_:))*