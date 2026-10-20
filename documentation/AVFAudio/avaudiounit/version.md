# version

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The version number of the audio unit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var version: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger version;
```

## See Also

### Getting Audio Unit values
- [var audioComponentDescription: AudioComponentDescription](./audiocomponentdescription.md)
  The audio component description that represents the underlying Core Audio audio unit.
- [var manufacturerName: String](./manufacturername.md)
  The name of the manufacturer of the audio unit.
- [var name: String](./name.md)
  The name of the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit/version)*