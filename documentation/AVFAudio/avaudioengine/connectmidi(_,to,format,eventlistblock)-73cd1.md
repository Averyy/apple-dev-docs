# connectMIDI(_:to:format:eventListBlock:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Establishes a MIDI connection between two nodes.

**Availability**:
- iOS 16.0+ - Deprecated in 27.0
- iPadOS 16.0+ - Deprecated in 27.0
- Mac Catalyst 16.0+ - Deprecated in 27.0
- macOS 13.0+ - Deprecated in 27.0
- tvOS 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

## Declaration

```swift
func connectMIDI(_ sourceNode: AVAudioNode, to destinationNode: AVAudioNode, format: AVAudioFormat?, eventListBlock tapBlock: AUMIDIEventListBlock? = nil)
```

```objc
- (void) connectMIDI:(AVAudioNode *) sourceNode to:(AVAudioNode *) destinationNode format:(AVAudioFormat *) format eventListBlock:(AUMIDIEventListBlock) tapBlock;
```

## Discussion

Use this to establish a MIDI connection between a source node and a destination node that has MIDI input capability. This method disconnects any existing MIDI connection that involves the destination node. When making the MIDI connection, this method overwrites the source node’s event list block.

The source node can only be an [`AVAudioUnit`](../avaudiounit.md) node with the type [`kAudioUnitType_MIDIProcessor`](../../AudioToolbox/kaudiounittype_midiprocessor.md). The destination node types can be [`kAudioUnitType_MusicDevice`](../../AudioToolbox/kaudiounittype_musicdevice.md), [`kAudioUnitType_MusicEffect`](../../AudioToolbox/kaudiounittype_musiceffect.md), or [`kAudioUnitType_MIDIProcessor`](../../AudioToolbox/kaudiounittype_midiprocessor.md).

## Parameters

- `sourceNode`: The source node.
- `destinationNode`: The destination node.
- `format`: If not `NULL`, the engine uses this value for the format of the source audio node’s output bus. In all cases, the engine matches the format of the destination audio node’s input bus to the source node’s output bus.
- `tapBlock`: If not `NULL`, the source node’s event list block calls this on the real-time thread. The host can tap the MIDI data of the source node through this block.

## See Also

### Managing MIDI nodes
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, eventListProvider: AVMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistprovider%29-8tmk8.md)
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, eventListProvider: AVMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistprovider%29-35k1c.md)
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, eventListBlock: AUMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistblock%29-7qtd5.md)
  Establishes a MIDI connection between a source node and multiple destination nodes.
- [func disconnectMIDI(AVAudioNode, from: AVAudioNode)](./disconnectmidi%28_,from%29-1kssy.md)
  Removes a MIDI connection between two nodes.
- [func disconnectMIDI(AVAudioNode, from: [AVAudioNode])](./disconnectmidi%28_,from%29-7oaab.md)
  Removes a MIDI connection between one source node and multiple destination nodes.
- [func disconnectMIDIInput(AVAudioNode)](./disconnectmidiinput%28_%29.md)
  Disconnects all input MIDI connections from a node.
- [func disconnectMIDIOutput(AVAudioNode)](./disconnectmidioutput%28_%29.md)
  Disconnects all output MIDI connections from a node.
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, block: AUMIDIOutputEventBlock?)](./connectmidi%28_,to,format,block%29-3bc13.md)
  Establishes a MIDI-only connection between two nodes.
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, block: AUMIDIOutputEventBlock?)](./connectmidi%28_,to,format,block%29-666bc.md)
  Establishes a MIDI-only connection between a source node and multiple destination nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connectmidi(_:to:format:eventlistblock:)-73cd1)*