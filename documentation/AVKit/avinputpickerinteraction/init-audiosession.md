# init(audioSession:)

**Framework**: AVKit  
**Kind**: init

Creates a new instance of AVInputPickerInteraction using a specific `AVAudioSession`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
init(audioSession: AVAudioSession?)
```

#### Discussion

Use this initializer when the provided `AVAudioSession` is in .record mode or you plan to switch it to record mode.

If nil session is passed in object will use a sharedInstance from `AVAudioSession`.

## Parameters

- `audioSession`: An optional recording configured audio session. If you provide a non-recording session, the input list will be empty.

## See Also

- [init()](avinputpickerinteraction/init.md)
  Creates a new instance of AVInputPickerController using a default sharedInstance from `AVAudioSession`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction/init(audiosession:))*