# init(audioComponentDescription:)

**Framework**: AVFAudio  
**Kind**: init

Creates a time effect audio unit with the specified description.

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

A new `AVAudioUnitTimeEffect` instance.

#### Discussion

The `componentType` field of the description structure must be `kAudioUnitType_FormatConverter` (”`aufc`”); otherwise, the method raises an exception.

## Parameters

- `audioComponentDescription`: The description of the audio unit to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounittimeeffect/init(audiocomponentdescription:))*