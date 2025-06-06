# connectMIDI(_:to:format:eventListBlock:)

**Framework**: AVFAudio  
**Kind**: method

Establishes a MIDI connection between a source node and multiple destination nodes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func connectMIDI(_ sourceNode: AVAudioNode, to destinationNodes: [AVAudioNode], format: AVAudioFormat?, eventListBlock tapBlock: AUMIDIEventListBlock? = nil)
```

#### Discussion

Use this to establish a MIDI connection between a source node and multiple destination nodes that have MIDI input capability. This method disconnects any existing MIDI connection that involves the destination node. When making the MIDI connection, this method overwrites the source node’s event list block.

The source node can only be an [`AVAudioUnit`](avaudiounit.md) node with the type [`kAudioUnitType_MIDIProcessor`](https://developer.apple.com/documentation/AudioToolbox/kAudioUnitType_MIDIProcessor). The destination node types can be [`kAudioUnitType_MusicDevice`](https://developer.apple.com/documentation/AudioToolbox/kAudioUnitType_MusicDevice), [`kAudioUnitType_MusicEffect`](https://developer.apple.com/documentation/AudioToolbox/kAudioUnitType_MusicEffect), or [`kAudioUnitType_MIDIProcessor`](https://developer.apple.com/documentation/AudioToolbox/kAudioUnitType_MIDIProcessor).

MIDI connections made with this method specify a single destination connection (one-to-one) or  multiple connections (one-to-many), but never many-to-one.

## Parameters

- `sourceNode`: The source node.
- `destinationNodes`: An array of objects that specify the destination nodes.
- `format`: If not  , the engine uses this value for the format of the source audio node’s output bus. In all cases, the format of the source node’s output bus has to match with the destination node’s output bus format.
- `tapBlock`: If not  , the source node’s event list block calls this on the real-time thread. The host can tap the MIDI data of the source node through this block.

## See Also

- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, eventListBlock: AUMIDIEventListBlock?)](avaudioengine/connectmidi(_:to:format:eventlistblock:)-73cd1.md)
  Establishes a MIDI connection between two nodes.
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
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, block: AUMIDIOutputEventBlock?)](avaudioengine/connectmidi(_:to:format:block:)-666bc.md)
  Establishes a MIDI-only connection between a source node and multiple destination nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connectmidi(_:to:format:eventlistblock:)-7qtd5)*