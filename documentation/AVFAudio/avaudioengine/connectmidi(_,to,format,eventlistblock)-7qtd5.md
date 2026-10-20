# connectMIDI(_:to:format:eventListBlock:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Establishes a MIDI connection between a source node and multiple destination nodes.

**Availability**:
- iOS 16.0+ - Deprecated in 27.0
- iPadOS 16.0+ - Deprecated in 27.0
- Mac Catalyst 16.0+ - Deprecated in 27.0
- macOS 13.0+ - Deprecated in 27.0
- tvOS 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

## Declaration

```swift
func connectMIDI(_ sourceNode: AVAudioNode, to destinationNodes: [AVAudioNode], format: AVAudioFormat?, eventListBlock tapBlock: AUMIDIEventListBlock? = nil)
```

```objc
- (void) connectMIDI:(AVAudioNode *) sourceNode toNodes:(NSArray<AVAudioNode *> *) destinationNodes format:(AVAudioFormat *) format eventListBlock:(AUMIDIEventListBlock) tapBlock;
```

#### Discussion

Use this to establish a MIDI connection between a source node and multiple destination nodes that have MIDI input capability. This method disconnects any existing MIDI connection that involves the destination node. When making the MIDI connection, this method overwrites the source node’s event list block.

The source node can only be an [`AVAudioUnit`](../avaudiounit.md) node with the type [`kAudioUnitType_MIDIProcessor`](../../AudioToolbox/kaudiounittype_midiprocessor.md). The destination node types can be [`kAudioUnitType_MusicDevice`](../../AudioToolbox/kaudiounittype_musicdevice.md), [`kAudioUnitType_MusicEffect`](../../AudioToolbox/kaudiounittype_musiceffect.md), or [`kAudioUnitType_MIDIProcessor`](../../AudioToolbox/kaudiounittype_midiprocessor.md).

MIDI connections made with this method specify a single destination connection (one-to-one) or  multiple connections (one-to-many), but never many-to-one.

## Parameters

- `sourceNode`: The source node.
- `destinationNodes`: An array of objects that specify the destination nodes.
- `format`: If not `NULL`, the engine uses this value for the format of the source audio node’s output bus. In all cases, the format of the source node’s output bus has to match with the destination node’s output bus format.
- `tapBlock`: If not `NULL`, the source node’s event list block calls this on the real-time thread. The host can tap the MIDI data of the source node through this block.

## See Also

### Managing MIDI nodes
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, eventListProvider: AVMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistprovider%29-8tmk8.md)
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, eventListProvider: AVMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistprovider%29-35k1c.md)
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, eventListBlock: AUMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistblock%29-73cd1.md)
  Establishes a MIDI connection between two nodes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connectmidi(_:to:format:eventlistblock:)-7qtd5)*