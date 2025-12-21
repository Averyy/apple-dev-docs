# AudioHardwareClock

**Framework**: Core Audio  
**Kind**: class

Instances of the AudioHardwareClock class encapsulate individual audio clocks. All audio devices inherit from the audio clock class, which provides several base properties and contains a list of control objects. Clock objects can be used as a time source when run in an aggregate device, but contain no IO streams.

**Availability**:
- Mac Catalyst ?+
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
  An array of AudioValueRange structs that indicates the valid ranges for the nominal sample rate of the device.
- [var clockDomain: UInt32](audiohardwareclock/clockdomain.md)
  A UInt32 whose value indicates the clock domain to which this object belongs. Clocks and devices that have the same value for this property are able to be synchronized in hardware.
- [var controls: [AudioHardwareControl]](audiohardwareclock/controls.md)
  An array of AudioHardwareControls that represent the controls of the device.
- [var inputLatency: Int](audiohardwareclock/inputlatency.md)
  An Int containing the number of frames of input latency in the clock.
- [var isAlive: Bool](audiohardwareclock/isalive.md)
  A Bool where a value of true indicates the device is ready and available and false indicates the device is unusable and will most likely go away shortly.
- [var isRunning: Bool](audiohardwareclock/isrunning.md)
  A Bool where a value of false indicates the device is not providing timestamps and a value of true means that it is.
- [var nominalSampleRate: Double](audiohardwareclock/nominalsamplerate.md)
  A Double that indicates the current nominal sample rate of the device.
- [var outputLatency: Int](audiohardwareclock/outputlatency.md)
  An Int containing the number of frames of output latency in the clock.
- [var transportType: UInt32](audiohardwareclock/transporttype.md)
  A UInt32 whose value indicates how the object is connected to the CPU. Constants for some of the values for this property can be found in the enum in the AudioDevice Constants section of AudioHardwareBase.h.
- [var uid: String](audiohardwareclock/uid.md)
  A String that contains a persistent identifier for the clock device. A clock’s UID is persistent across boots. The content of the UID string is a black box and may contain information that is unique to a particular instance of an clock’s hardware or unique to the CPU. Therefore they are not suitable for passing between CPUs or for identifying similar models of hardware.
### Instance Methods
- [func setNominalSampleRate(Double) throws](audiohardwareclock/setnominalsamplerate(_:).md)
  Set the nominalSampleRate property.

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Inherited By
- [AudioHardwareDevice](audiohardwaredevice.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareclock)*