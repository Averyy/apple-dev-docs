# init(audioComponentDescription:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio unit effect object with the specified description.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(audioComponentDescription: AudioComponentDescription)
```

#### Return Value

A new `AVAudioUnitEffect` instance.

## Parameters

- `audioComponentDescription`: The description of the audio unit to create. The `audioComponentDescription` must be one of these types `kAudioUnitType_Effect`, `kAudioUnitType_MusicEffect`, `kAudioUnitType_Panner`, `kAudioUnitType_RemoteEffect`, or `kAudioUnitType_RemoteMusicEffect`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteffect/init(audiocomponentdescription:))*