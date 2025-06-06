# destinationMIDIEndpoint

**Framework**: AVFAudio  
**Kind**: property

The MIDI endpoint you specify as the track’s target.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var destinationMIDIEndpoint: MIDIEndpointRef { get set }
```

#### Discussion

This property and a [`destinationAudioUnit`](avmusictrack/destinationaudiounit.md) are mutually exclusive. Setting this property removes the track’s reference to an [`AVAudioUnit`](avaudiounit.md) destination. When playing, the track sends events to the MIDI endpoint. For more information, see [`MIDIDestinationCreate(_:_:_:_:_:)`](https://developer.apple.com/documentation/CoreMIDI/MIDIDestinationCreate(_:_:_:_:_:)). You can’t change the endpoint while the track’s sequence is in a playing state.

## See Also

- [var destinationAudioUnit: AVAudioUnit?](avmusictrack/destinationaudiounit.md)
  The audio unit that receives the track’s events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/destinationmidiendpoint)*