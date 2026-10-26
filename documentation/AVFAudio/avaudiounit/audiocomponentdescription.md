# audioComponentDescription

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio component description that represents the underlying Core Audio audio unit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var audioComponentDescription: AudioComponentDescription { get }
```

```objc
@property (nonatomic, readonly) AudioComponentDescription audioComponentDescription;
```

## See Also

### Related Documentation
- [func withAudioUnit<R, E>((borrowing AudioUnit) throws(E) -> R) throws(E) -> R](./withaudiounit%28_%29-66uo7.md)
  Provides scoped access to the audio unit’s AudioUnit
- [func withAudioUnit<R, E>((borrowing AudioUnit) throws(E) -> R) throws(E) -> R](./withaudiounit%28_%29-6c2ze.md)
  Provides scoped access to the audio unit’s AudioUnit
- [audioUnit](./audiounit-4wpas.md)
  The underlying Core Audio audio unit.
### Getting Audio Unit values
- [var manufacturerName: String](./manufacturername.md)
  The name of the manufacturer of the audio unit.
- [var name: String](./name.md)
  The name of the audio unit.
- [var version: Int](./version.md)
  The version number of the audio unit.
- [AUAudioUnit](./auaudiounit.md)
  The audio unit class wrapping or underlying the implementation’s audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit/audiocomponentdescription)*