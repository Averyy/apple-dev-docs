# AudioDeviceRemovePropertyListener

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus AudioDeviceRemovePropertyListener(AudioDeviceID inDevice, UInt32 inChannel, Boolean isInput, AudioDevicePropertyID inPropertyID, AudioDevicePropertyListenerProc inProc);
```

## Return Value

An OSStatus indicating success or failure.

## Discussion

Unregisters the given AudioDevicePropertyListenerProc from receiving notifications when the given property changes.

Note that the same functionality is provided by AudioObjectRemovePropertyListener in conjunction with AudioObjectPropertyListenerProc.

## Parameters

- `inDevice`: The AudioDevice with whom to unregister the listener.
- `inChannel`: The channel of the property to unregister from.
- `isInput`: Which section of the AudioDevice to unregister from.
- `inPropertyID`: The AudioDevicePropertyID of the property to stop listening to.
- `inProc`: AudioDevicePropertyListenerProc to unregister.

## See Also

### Deprecated Functions
- [AudioDeviceAddIOProc](./audiodeviceaddioproc.md)
- [AudioDeviceAddPropertyListener](./audiodeviceaddpropertylistener.md)
- [AudioDeviceGetProperty](./audiodevicegetproperty.md)
- [AudioDeviceGetPropertyInfo](./audiodevicegetpropertyinfo.md)
- [AudioDeviceRead](./audiodeviceread.md)
- [AudioDeviceRemoveIOProc](./audiodeviceremoveioproc.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodeviceremovepropertylistener)*