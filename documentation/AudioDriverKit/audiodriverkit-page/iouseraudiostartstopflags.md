# IOUserAudioStartStopFlags

**Framework**: AudioDriverKit  
**Kind**: enum  
**Role**: Enumeration

Values that indicate I/O starts or stops.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
enum IOUserAudioStartStopFlags : uint64_t;
```

## Topics

### Start/Stop Behaviors
- [None](./iouseraudiostartstopflags/none.md)
  A flag that indicates starting or stopping for normal I/O operation.
- [Prewarm](./iouseraudiostartstopflags/prewarm.md)
  A flag that indicates starting or stopping for prewarming.

## See Also

### Performing I/O
- [StartIO](../iouseraudioclockdevice/startio.md)
  Tells the clock device to start I/O.
- [StopIO](../iouseraudioclockdevice/stopio.md)
  Tells the clock device to stop I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiostartstopflags)*