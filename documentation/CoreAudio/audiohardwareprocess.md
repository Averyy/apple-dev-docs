# AudioHardwareProcess

**Framework**: Core Audio  
**Kind**: class

Instances of the AudioHardwareProcess class encapsulate a single audio process, which contains information about a client process connected to the HAL.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
class AudioHardwareProcess
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwareprocess/init(id:).md)
### Instance Properties
- [var bundleID: String?](audiohardwareprocess/bundleid.md)
  A String that contains the bundle ID of the process.
- [var devices: [AudioHardwareDevice]](audiohardwareprocess/devices.md)
  An array of AudioHardwareDevices that represent the devices currently used by the process for output.
- [var isRunning: Bool](audiohardwareprocess/isrunning.md)
  A Bool where a value of true indicates that there is audio IO in progress in the process.
- [var isRunningInput: Bool](audiohardwareprocess/isrunninginput.md)
  A Bool where a value of true indicates that the process is running IO and there is at least one active input stream.
- [var isRunningOutput: Bool](audiohardwareprocess/isrunningoutput.md)
  A Bool where a value of true indicates that the process is running IO and there is at least one active output stream.
- [var pid: pid_t](audiohardwareprocess/pid.md)
  A pid_t indicating the process ID associated with the process.

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareprocess)*