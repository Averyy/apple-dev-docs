# outputNode

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio engine’s singleton output audio node.

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
var outputNode: AVAudioOutputNode { get }
```

```objc
@property (nonatomic, readonly) AVAudioOutputNode * outputNode;
```

## Discussion

The framework performs audio output through an output node. The audio engine creates a singleton on demand when first accessing this variable. Connect another node to the input of the output node, or get a mixer using the [`mainMixerNode`](./mainmixernode.md) property.

When the engine renders to and from an audio device, the [`AVAudioSession`](../avaudiosession.md) category and the availability of hardware determines whether an app performs output. Check the output node’s output format (specifically, the hardware format) for a nonzero sample rate and channel count to see if output is in an enabled state.

Trying to perform output through the output node when it isn’t available or in an enabled state causes the engine to throw an error (when possible) or an exception.

In manual rendering mode, the output node’s format determines the render format of the engine. For more information about changing it, see [`enableManualRenderingMode(_:format:maximumFrameCount:)`](./enablemanualrenderingmode%28_,format,maximumframecount%29.md).

## See Also

### Accessing the built-in nodes
- [var inputNode: AVAudioInputNode](./inputnode.md)
  The audio engine’s singleton input audio node.
- [var mainMixerNode: AVAudioMixerNode](./mainmixernode.md)
  The audio engine’s optional singleton main mixer node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/outputnode)*