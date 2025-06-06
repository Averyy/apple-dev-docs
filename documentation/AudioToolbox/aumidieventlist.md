# AUMIDIEventList

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AUMIDIEventList
```

## Topics

### Initializers
- [init()](aumidieventlist/init.md)
- [init(next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: UInt8, cable: UInt8, eventList: MIDIEventList)](aumidieventlist/init(next:eventsampletime:eventtype:reserved:cable:eventlist:).md)
### Instance Properties
- [var cable: UInt8](aumidieventlist/cable.md)
- [var eventList: MIDIEventList](aumidieventlist/eventlist.md)
- [var eventSampleTime: AUEventSampleTime](aumidieventlist/eventsampletime.md)
- [var eventType: AURenderEventType](aumidieventlist/eventtype.md)
- [var next: UnsafeMutablePointer<AURenderEvent>?](aumidieventlist/next.md)
- [var reserved: UInt8](aumidieventlist/reserved.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioConverterOptions](audioconverteroptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aumidieventlist)*