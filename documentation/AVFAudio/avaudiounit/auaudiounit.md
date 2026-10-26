# AUAudioUnit

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio unit class wrapping or underlying the implementation’s audio unit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) AUAudioUnit * AUAudioUnit;
```

## See Also

### Getting Audio Unit values
- [var audioComponentDescription: AudioComponentDescription](./audiocomponentdescription.md)
  The audio component description that represents the underlying Core Audio audio unit.
- [var manufacturerName: String](./manufacturername.md)
  The name of the manufacturer of the audio unit.
- [var name: String](./name.md)
  The name of the audio unit.
- [var version: Int](./version.md)
  The version number of the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit/auaudiounit)*