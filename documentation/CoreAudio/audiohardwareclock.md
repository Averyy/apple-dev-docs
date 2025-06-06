# AudioHardwareClock

**Framework**: Core Audio  
**Kind**: class

**Availability**:
- macOS 15.0+

## Declaration

```swift
class AudioHardwareClock
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwareclock/init(id:).md)
### Instance Properties
- [var availableNominalSampleRates: [AudioValueRange]](audiohardwareclock/availablenominalsamplerates.md)
- [var clockDomain: UInt32](audiohardwareclock/clockdomain.md)
- [var controls: [AudioHardwareControl]](audiohardwareclock/controls.md)
- [var inputLatency: Int](audiohardwareclock/inputlatency.md)
- [var isAlive: Bool](audiohardwareclock/isalive.md)
- [var isRunning: Bool](audiohardwareclock/isrunning.md)
- [var nominalSampleRate: Double](audiohardwareclock/nominalsamplerate.md)
- [var outputLatency: Int](audiohardwareclock/outputlatency.md)
- [var transportType: UInt32](audiohardwareclock/transporttype.md)
- [var uid: String](audiohardwareclock/uid.md)
### Instance Methods
- [func setNominalSampleRate(Double) throws](audiohardwareclock/setnominalsamplerate(_:).md)

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Inherited By
- [AudioHardwareDevice](audiohardwaredevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareclock)*