# mixer

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The audio stream’s output pipeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var mixer: PHASEMixer { get }
```

```objc
@property (nonatomic, strong, readonly) PHASEMixer * mixer;
```

#### Discussion

The framework sets the value based on the definition initializer’s `mixerDefinition` argument. See [`init(mixerDefinition:format:)`](../phasepushstreamnodedefinition/init%28mixerdefinition,format%29.md).

## See Also

### Inspecting Stream Properties
- [var format: AVAudioFormat](./format.md)
  The format of the audio stream data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnode/mixer)*