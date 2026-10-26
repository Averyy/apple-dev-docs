# AudioHardwareRemovePropertyListener

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus AudioHardwareRemovePropertyListener(AudioHardwarePropertyID inPropertyID, AudioHardwarePropertyListenerProc inProc);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Unregisters the given AudioHardwarePropertyListenerProc from receive notifications when the given property changes.

Note that the same functionality is provided by AudioObjectRemovePropertyListener in conjunction with AudioObjectPropertyListenerProc.

## Parameters

- `inPropertyID`: The AudioHardwarePropertyID of the property to stop listening to.
- `inProc`: AudioHardwarePropertyListenerProc to unregister.

## See Also

### Deprecated Functions
- [AudioDeviceAddIOProc](./audiodeviceaddioproc.md)
- [AudioDeviceAddPropertyListener](./audiodeviceaddpropertylistener.md)
- [AudioDeviceGetProperty](./audiodevicegetproperty.md)
- [AudioDeviceGetPropertyInfo](./audiodevicegetpropertyinfo.md)
- [AudioDeviceRead](./audiodeviceread.md)
- [AudioDeviceRemoveIOProc](./audiodeviceremoveioproc.md)
- [AudioDeviceRemovePropertyListener](./audiodeviceremovepropertylistener.md)
- [AudioDeviceSetProperty](./audiodevicesetproperty.md)
- [AudioHardwareAddPropertyListener](./audiohardwareaddpropertylistener.md)
- [AudioHardwareAddRunLoopSource](./audiohardwareaddrunloopsource.md)
- [AudioHardwareGetProperty](./audiohardwaregetproperty.md)
- [AudioHardwareGetPropertyInfo](./audiohardwaregetpropertyinfo.md)
- [AudioHardwareRemoveRunLoopSource](./audiohardwareremoverunloopsource.md)
- [AudioHardwareSetProperty](./audiohardwaresetproperty.md)
- [AudioStreamAddPropertyListener](./audiostreamaddpropertylistener.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareremovepropertylistener)*