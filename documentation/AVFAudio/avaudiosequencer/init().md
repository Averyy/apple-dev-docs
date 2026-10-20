# init()

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates an audio sequencer object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Discussion

Use this initializer to create a sequencer with tracks that only send events to external MIDI endpoints.

## See Also

### Creating an audio sequencer
- [init(audioEngine: AVAudioEngine)](./init%28audioengine%29.md)
  Creates an audio sequencer that the framework attaches to an audio engine instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/init())*