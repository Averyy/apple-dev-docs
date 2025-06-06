# init(next:eventSampleTime:eventType:reserved:rampDurationSampleFrames:parameterAddress:value:)

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
init(next: UnsafeMutablePointer<AURenderEvent>?, eventSampleTime: AUEventSampleTime, eventType: AURenderEventType, reserved: (UInt8, UInt8, UInt8), rampDurationSampleFrames: AUAudioFrameCount, parameterAddress: AUParameterAddress, value: AUValue)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameterevent/init(next:eventsampletime:eventtype:reserved:rampdurationsampleframes:parameteraddress:value:))*