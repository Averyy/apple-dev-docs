# AudioStreamAddPropertyListener

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.1+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus AudioStreamAddPropertyListener(AudioStreamID inStream, UInt32 inChannel, AudioDevicePropertyID inPropertyID, AudioStreamPropertyListenerProc inProc, void *inClientData);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Registers the given AudioStreamPropertyListenerProc to receive notifications when the given property changes.

Note that the same functionality is provided by AudioObjectAddPropertyListener in conjunction with AudioObjectPropertyListenerProc.

## Parameters

- `inStream`: The AudioStream with whom to register the listener.
- `inChannel`: The channel of the property to listen to.
- `inPropertyID`: The AudioDevicePropertyID of the property to listen to.
- `inProc`: AudioStreamPropertyListenerProc to call.
- `inClientData`: A pointer to client data that is passed to the listener when it is called.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiostreamaddpropertylistener)*