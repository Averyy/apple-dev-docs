# init(mixerDefinition:format:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a node definition for audio streams.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(mixerDefinition: PHASEMixerDefinition, format: AVAudioFormat)
```

```objc
- (instancetype) initWithMixerDefinition:(PHASEMixerDefinition *) mixerDefinition format:(AVAudioFormat *) format;
```

## Parameters

- `mixerDefinition`: An object that combines audio layers.
- `format`: The format of the audio stream data.

## See Also

### Creating a Node
- [convenience init(mixerDefinition: PHASEMixerDefinition, format: AVAudioFormat, identifier: String)](./init%28mixerdefinition,format,identifier%29.md)
  Creates a named node definition for audio streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnodedefinition/init(mixerdefinition:format:))*