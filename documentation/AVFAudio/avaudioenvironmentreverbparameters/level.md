# level

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Controls the amount of reverb, in decibels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var level: Float { get set }
```

```objc
@property (nonatomic) float level;
```

## Discussion

The default value is `0.0`. The values must be within the range of `-40` to `40` dB.

## See Also

### Getting and setting reverb values
- [var filterParameters: AVAudioUnitEQFilterParameters](./filterparameters.md)
  A filter that the system applies to the output.
- [func loadFactoryReverbPreset(AVAudioUnitReverbPreset)](./loadfactoryreverbpreset%28_%29.md)
  Loads one of the reverbs factory presets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentreverbparameters/level)*