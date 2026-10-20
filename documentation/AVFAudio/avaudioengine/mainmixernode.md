# mainMixerNode

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio engine’s optional singleton main mixer node.

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
var mainMixerNode: AVAudioMixerNode { get }
```

```objc
@property (nonatomic, readonly) AVAudioMixerNode * mainMixerNode;
```

#### Discussion

The audio engine constructs a singleton main mixer and connects it to the [`outputNode`](./outputnode.md) when first accessing this property. You can then connect additional audio nodes to the mixer.

If the client never sets the connection format between the `mainMixerNode` and the `outputNode`, the engine always updates the format to track the format of the `outputNode` on startup or restart, even after an [`AVAudioEngineConfigurationChangeNotification`](../avaudioengineconfigurationchangenotification.md). Otherwise, it’s the client’s responsibility to update the connection format after an [`AVAudioEngineConfigurationChangeNotification`](../avaudioengineconfigurationchangenotification.md).

By default, the mixer’s output format (sample rate and channel count) tracks the format of the output node.

## See Also

### Accessing the built-in nodes
- [var inputNode: AVAudioInputNode](./inputnode.md)
  The audio engine’s singleton input audio node.
- [var outputNode: AVAudioOutputNode](./outputnode.md)
  The audio engine’s singleton output audio node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/mainmixernode)*