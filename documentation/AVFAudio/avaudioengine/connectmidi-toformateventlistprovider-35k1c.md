# connectMIDI(_:to:format:eventListProvider:)

**Framework**: AVFAudio  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func connectMIDI(_ sourceNode: AVAudioNode, to destinationNodes: [AVAudioNode], format: AVAudioFormat?, eventListProvider tapBlock: AVMIDIEventListBlock? = nil)
```

#### Discussion

Establish a MIDI only connection between a source node and multiple destination nodes.

Use this method to establish a MIDI only connection between a source node and multiple destination nodes.

The source node can only be a AVAudioUnit node of type `kAudioUnitType_MIDIProcessor`. The destination node types can be `kAudioUnitType_MusicDevice`, `kAudioUnitType_MusicEffect` or `kAudioUnitType_MIDIProcessor`.

MIDI connections made using this method are either one-to-one (when a single destination connection is specified) or one-to-many (when multiple connections are specified), but never many-to-one.

Note that any pre-existing connection involving the destination will be broken.

Any client installed block on the source node’s audio unit `AUMIDIOutputEventListBlock` will be overwritten when making the MIDI connection.

## Parameters

- `sourceNode`: The source node.
- `destinationNodes`: An array of AVAudioNodes specifying destination nodes.
- `format`: If non-nil, the format of the source node’s output bus is set to this format. In all cases, the format of the source nodes’ output bus has to match with the destination nodes’ output bus format. Although the output bus of the source is not in use, the format needs to be set in order to be able to use the sample rate for MIDI event timing calculations.
- `tapBlock`: This block is called from the source node’s `AUMIDIOutputEventListBlock` on the realtime thread. The host can tap the MIDI data of the source node through this block.

## See Also

- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, eventListProvider: AVMIDIEventListBlock?)](avaudioengine/connectmidi(_:to:format:eventlistprovider:)-8tmk8.md)
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
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, block: AUMIDIOutputEventBlock?)](avaudioengine/connectmidi(_:to:format:block:)-666bc.md)
  Establishes a MIDI-only connection between a source node and multiple destination nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connectmidi(_:to:format:eventlistprovider:)-35k1c)*