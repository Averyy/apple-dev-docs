# data128

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

active when type is kMIDIMessageTypeData128

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
struct { ... } data128;
```

## Topics

### Instance Properties
- [mixedDataSet](./data128-43npl/mixeddataset.md)
  active when status is kMIDISysExStatusMixedDataSetHeader or kMIDISysExStatusMixedDataSetPayload
- [status](./data128-43npl/status.md)
  determines which variant is active
- [sysex8](./data128-43npl/sysex8.md)
  active when status any of kMIDISysExStatusComplete, kMIDISysExStatusStart, kMIDISysExStatusContinue, or kMIDISysExStatusEnd


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiuniversalmessage/data128-43npl)*