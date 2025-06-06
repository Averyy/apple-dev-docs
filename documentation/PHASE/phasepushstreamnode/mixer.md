# mixer

**Framework**: PHASE  
**Kind**: property

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

#### Discussion

The framework sets the value based on the definition initializer’s `mixerDefinition` argument. See [`init(mixerDefinition:format:)`](phasepushstreamnodedefinition/init(mixerdefinition:format:).md).

## See Also

- [var format: AVAudioFormat](phasepushstreamnode/format.md)
  The format of the audio stream data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnode/mixer)*