# filterParameters

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A filter that the system applies to the output.

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
var filterParameters: AVAudioUnitEQFilterParameters { get }
```

```objc
@property (nonatomic, readonly) AVAudioUnitEQFilterParameters * filterParameters;
```

## See Also

### Getting and setting reverb values
- [var level: Float](./level.md)
  Controls the amount of reverb, in decibels.
- [func loadFactoryReverbPreset(AVAudioUnitReverbPreset)](./loadfactoryreverbpreset%28_%29.md)
  Loads one of the reverbs factory presets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentreverbparameters/filterparameters)*