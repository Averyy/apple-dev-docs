# AudioDeviceRead

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.1+ - Deprecated in 10.5

## Declaration

```c
extern OSStatus AudioDeviceRead(AudioDeviceID inDevice, const AudioTimeStamp *inStartTime, AudioBufferList *outData);
```

#### Return Value

An OSStatus indicating success or failure. kAudioHardwareUnsupportedOperationError will be returned if the AudioDevice does not support direct reading.

#### Discussion

Read some data from an AudioDevice starting at the given time.

With the advent of aggregate devices, the need for AudioDeviceRead has gone away. Consequently, this function is now deprecated.

## Parameters

- `inDevice`: The AudioDevice to read from.
- `inStartTime`: An AudioTimeStamp indicating the time from which to read the data. In general, the valid range of time (in frames) is from the current time minus the maximum IO buffer size to the current time minus the safety offset.
- `outData`: An AudioBufferList that must be the same size and shape as that returned by kAudioDevicePropertyStreamConfiguration. Further, the AudioBufferList must have been previously registered with the device via kAudioDevicePropertyRegisterBufferList. On exit, the mDataSize fields will be updated with the amount of data read.

## See Also

### Deprecated Functions
- [AudioDeviceAddIOProc](./audiodeviceaddioproc.md)
- [AudioDeviceAddPropertyListener](./audiodeviceaddpropertylistener.md)
- [AudioDeviceGetProperty](./audiodevicegetproperty.md)
- [AudioDeviceGetPropertyInfo](./audiodevicegetpropertyinfo.md)
- [AudioDeviceRemoveIOProc](./audiodeviceremoveioproc.md)
- [AudioDeviceRemovePropertyListener](./audiodeviceremovepropertylistener.md)
- [AudioDeviceSetProperty](./audiodevicesetproperty.md)
- [AudioHardwareAddPropertyListener](./audiohardwareaddpropertylistener.md)
- [AudioHardwareAddRunLoopSource](./audiohardwareaddrunloopsource.md)
- [AudioHardwareGetProperty](./audiohardwaregetproperty.md)
- [AudioHardwareGetPropertyInfo](./audiohardwaregetpropertyinfo.md)
- [AudioHardwareRemovePropertyListener](./audiohardwareremovepropertylistener.md)
- [AudioHardwareRemoveRunLoopSource](./audiohardwareremoverunloopsource.md)
- [AudioHardwareSetProperty](./audiohardwaresetproperty.md)
- [AudioStreamAddPropertyListener](./audiostreamaddpropertylistener.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodeviceread)*