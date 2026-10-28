# format

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The format of the audio stream data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var format: AVAudioFormat { get }
```

```objc
@property (nonatomic, strong, readonly) AVAudioFormat * format;
```

## Discussion

The framework sets the value to the [`init(mixerDefinition:format:)`](../phasepushstreamnodedefinition/init%28mixerdefinition,format%29.md) argument.

## See Also

### Inspecting Stream Properties
- [var mixer: PHASEMixer](./mixer.md)
  The audio stream’s output pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnode/format)*