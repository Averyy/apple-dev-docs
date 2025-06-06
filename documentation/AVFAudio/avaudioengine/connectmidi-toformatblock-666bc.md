# connectMIDI(_:to:format:block:)

**Framework**: AVFAudio  
**Kind**: method

Establishes a MIDI-only connection between a source node and multiple destination nodes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func connectMIDI(_ sourceNode: AVAudioNode, to destinationNodes: [AVAudioNode], format: AVAudioFormat?, block tapBlock: AUMIDIOutputEventBlock? = nil)
```

## Parameters

- `sourceNode`: The source node.
- `destinationNodes`: An array of   objects that specify destination nodes.
- `format`: If not  , the engine uses this value for the format of the source audio node’s output bus. In all cases, the format of the source node’s output bus has to match with the destination node’s output bus format.
- `tapBlock`: If not  , the source node’s   calls this block on the real-time thread. The host can tap the MIDI data of the source node through this block.

## See Also

- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, eventListBlock: AUMIDIEventListBlock?)](avaudioengine/connectmidi(_:to:format:eventlistblock:)-73cd1.md)
  Establishes a MIDI connection between two nodes.
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, eventListBlock: AUMIDIEventListBlock?)](avaudioengine/connectmidi(_:to:format:eventlistblock:)-7qtd5.md)
  Establishes a MIDI connection between a source node and multiple destination nodes.
- [func disconnectMIDI(AVAudioNode, from: AVAudioNode)](avaudioengine/disconnectmidi(_:from:)-1kssy.md)
  Removes a MIDI connection between two nodes.
- [func disconnectMIDI(AVAudioNode, from: [AVAudioNode])](avaudioengine/disconnectmidi(_:from:)-7oaab.md)
  Removes a MIDI connection between one source node and multiple destination nodes.
- [func disconnectMIDIInput(AVAudioNode)](avaudioengine/disconnectmidiinput(_:).md)
  Disconnects all input MIDI connections from a node.
- [func disconnectMIDIOutput(AVAudioNode)](avaudioengine/disconnectmidioutput(_:).md)
  Disconnects all output MIDI connections from a node.
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, block: AUMIDIOutputEventBlock?)](avaudioengine/connectmidi(_:to:format:block:)-3bc13.md)
  Establishes a MIDI-only connection between two nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connectmidi(_:to:format:block:)-666bc)*