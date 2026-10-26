# init(version:numSources:sources:numDestinations:destinations:channelMap:lowVelocity:highVelocity:lowNote:highNote:noteNumber:velocity:keyPressure:channelPressure:programChange:pitchBend:filterOutSysEx:filterOutMTC:filterOutBeatClock:filterOutTuneRequest:reserved2:filterOutAllControls:numControlTransforms:numMaps:reserved3:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(version: UInt32, numSources: UInt32, sources: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint), numDestinations: UInt32, destinations: (MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint, MIDIThruConnectionEndpoint), channelMap: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), lowVelocity: UInt8, highVelocity: UInt8, lowNote: UInt8, highNote: UInt8, noteNumber: MIDITransform, velocity: MIDITransform, keyPressure: MIDITransform, channelPressure: MIDITransform, programChange: MIDITransform, pitchBend: MIDITransform, filterOutSysEx: UInt8, filterOutMTC: UInt8, filterOutBeatClock: UInt8, filterOutTuneRequest: UInt8, reserved2: (UInt8, UInt8, UInt8), filterOutAllControls: UInt8, numControlTransforms: UInt16, numMaps: UInt16, reserved3: (UInt16, UInt16, UInt16, UInt16))
```

## See Also

### Initializers
- [init()](./init%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midithruconnectionparams/init(version:numsources:sources:numdestinations:destinations:channelmap:lowvelocity:highvelocity:lownote:highnote:notenumber:velocity:keypressure:channelpressure:programchange:pitchbend:filteroutsysex:filteroutmtc:filteroutbeatclock:filtero-6y1ig)*