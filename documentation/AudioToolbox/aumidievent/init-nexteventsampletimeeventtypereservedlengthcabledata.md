# init(next:eventSampleTime:eventType:reserved:length:cable:data:)

**Framework**: Audio Toolbox  
**Kind**: init

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: UInt8, length: UInt16, cable: UInt8, data: (UInt8, UInt8, UInt8))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aumidievent/init(next:eventsampletime:eventtype:reserved:length:cable:data:))*