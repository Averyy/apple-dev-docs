# AudioDeviceID

**Framework**: Core Audio  
**Kind**: typealias

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias AudioDeviceID = AudioObjectID
```

#### Discussion

AudioDevice is the base class for all objects that represent an audio device.

AudioDevice is a subclass of AudioObject. AudioDevices normally contain AudioStreams and AudioControls, but may contain other things depending on the kind of AudioDevice (e.g. aggregate devices contain other AudioDevices).

## See Also

- [typealias AudioClassID](audioclassid.md)
- [typealias AudioDeviceIOBlock](audiodeviceioblock.md)
- [typealias AudioDeviceIOProc](audiodeviceioproc.md)
- [typealias AudioDeviceIOProcID](audiodeviceioprocid.md)
- [typealias AudioDevicePropertyID](audiodevicepropertyid.md)
- [typealias AudioDevicePropertyListenerProc](audiodevicepropertylistenerproc.md)
- [typealias AudioHardwarePropertyID](audiohardwarepropertyid.md)
- [typealias AudioHardwarePropertyListenerProc](audiohardwarepropertylistenerproc.md)
- [typealias AudioObjectID](audioobjectid.md)
- [typealias AudioObjectPropertyElement](audioobjectpropertyelement.md)
- [typealias AudioObjectPropertyListenerBlock](audioobjectpropertylistenerblock.md)
- [typealias AudioObjectPropertyListenerProc](audioobjectpropertylistenerproc.md)
- [typealias AudioObjectPropertyScope](audioobjectpropertyscope.md)
- [typealias AudioObjectPropertySelector](audioobjectpropertyselector.md)
- [typealias AudioStreamID](audiostreamid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodeviceid)*