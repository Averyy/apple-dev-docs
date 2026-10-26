# AudioDeviceAddPropertyListener

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus AudioDeviceAddPropertyListener(AudioDeviceID inDevice, UInt32 inChannel, Boolean isInput, AudioDevicePropertyID inPropertyID, AudioDevicePropertyListenerProc inProc, void *inClientData);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Registers the given AudioDevicePropertyListenerProc to receive notifications when the given property changes.

Note that the same functionality is provided by AudioObjectAddPropertyListener in conjunction with AudioObjectPropertyListenerProc.

## Parameters

- `inDevice`: The AudioDevice with whom to register the listener.
- `inChannel`: The channel of the property to listen to.
- `isInput`: Which section of the AudioDevice to listen to.
- `inPropertyID`: The AudioDevicePropertyID of the property to listen to.
- `inProc`: AudioDevicePropertyListenerProc to call.
- `inClientData`: A pointer to client data that is passed to the listener when it is called.

## See Also

### Deprecated Functions
- [AudioDeviceAddIOProc](./audiodeviceaddioproc.md)
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
- [AudioStreamAddPropertyListener](./audiostreamaddpropertylistener.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodeviceaddpropertylistener)*