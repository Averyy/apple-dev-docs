# init(audioComponentDescription:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a generator audio unit with the specified description.

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

```objc
- (instancetype) initWithAudioComponentDescription:(AudioComponentDescription) audioComponentDescription;
```

#### Return Value

A new `AVAudioUnitGenerator` instance.

#### Discussion

The [`AudioComponentDescription`](../../AudioToolbox/audiocomponentdescription.md) structure `componentType` field must be `kAudioUnitType_Generator` or [`kAudioUnitType_RemoteGenerator`](../../AudioToolbox/kaudiounittype_remotegenerator.md).

## Parameters

- `audioComponentDescription`: The audio component description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitgenerator/init(audiocomponentdescription:))*