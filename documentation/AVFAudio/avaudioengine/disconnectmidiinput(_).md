# disconnectMIDIInput(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Disconnects all input MIDI connections from a node.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func disconnectMIDIInput(_ node: AVAudioNode)
```

```objc
- (void) disconnectMIDIInput:(AVAudioNode *) node;
```

## Parameters

- `node`: The node with the MIDI input to disconnect.

## See Also

### Managing MIDI nodes
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, eventListProvider: AVMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistprovider%29-8tmk8.md)
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, eventListProvider: AVMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistprovider%29-35k1c.md)
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, eventListBlock: AUMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistblock%29-73cd1.md)
  Establishes a MIDI connection between two nodes.
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, eventListBlock: AUMIDIEventListBlock?)](./connectmidi%28_,to,format,eventlistblock%29-7qtd5.md)
  Establishes a MIDI connection between a source node and multiple destination nodes.
- [func disconnectMIDI(AVAudioNode, from: AVAudioNode)](./disconnectmidi%28_,from%29-1kssy.md)
  Removes a MIDI connection between two nodes.
- [func disconnectMIDI(AVAudioNode, from: [AVAudioNode])](./disconnectmidi%28_,from%29-7oaab.md)
  Removes a MIDI connection between one source node and multiple destination nodes.
- [func disconnectMIDIOutput(AVAudioNode)](./disconnectmidioutput%28_%29.md)
  Disconnects all output MIDI connections from a node.
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, block: AUMIDIOutputEventBlock?)](./connectmidi%28_,to,format,block%29-3bc13.md)
  Establishes a MIDI-only connection between two nodes.
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, block: AUMIDIOutputEventBlock?)](./connectmidi%28_,to,format,block%29-666bc.md)
  Establishes a MIDI-only connection between a source node and multiple destination nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/disconnectmidiinput(_:))*