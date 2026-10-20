# init(mixerDefinition:format:identifier:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a named node definition for audio streams.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(mixerDefinition: PHASEMixerDefinition, format: AVAudioFormat, identifier: String)
```

```objc
- (instancetype) initWithMixerDefinition:(PHASEMixerDefinition *) mixerDefinition format:(AVAudioFormat *) format identifier:(NSString *) identifier;
```

## Parameters

- `mixerDefinition`: An object that combines audio layers.
- `format`: The format of the audio stream data.
- `identifier`: A unique name for the node.

## See Also

### Creating a Node
- [init(mixerDefinition: PHASEMixerDefinition, format: AVAudioFormat)](./init%28mixerdefinition,format%29.md)
  Creates a node definition for audio streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnodedefinition/init(mixerdefinition:format:identifier:))*