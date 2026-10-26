# AudioStreamRemovePropertyListener

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.1+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus AudioStreamRemovePropertyListener(AudioStreamID inStream, UInt32 inChannel, AudioDevicePropertyID inPropertyID, AudioStreamPropertyListenerProc inProc);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Unregisters the given AudioStreamPropertyListenerProc from receiving notifications when the given property changes.

Note that the same functionality is provided by AudioObjectRemovePropertyListener in conjunction with AudioObjectPropertyListenerProc.

## Parameters

- `inStream`: The AudioStream with whom to unregister the listener.
- `inChannel`: The channel of the property to unregister from.
- `inPropertyID`: The AudioDevicePropertyID of the property to stop listening to.
- `inProc`: AudioStreamPropertyListenerProc to unregister.

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
- [AudioHardwareRemovePropertyListener](./audiohardwareremovepropertylistener.md)
- [AudioHardwareRemoveRunLoopSource](./audiohardwareremoverunloopsource.md)
- [AudioHardwareSetProperty](./audiohardwaresetproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiostreamremovepropertylistener)*