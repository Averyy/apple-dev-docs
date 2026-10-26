# AudioDeviceAddIOProc

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```c
extern OSStatus AudioDeviceAddIOProc(AudioDeviceID inDevice, AudioDeviceIOProc inProc, void *inClientData);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Registers the given AudioDeviceIOProc with the AudioDevice.

A client may have multiple IOProcs for a given device, but the device is free to only accept as many as it can handle. Note that it is not recommended for clients to have more than a single IOProc registered at a time as this can be wasteful of system resources. Rather, it is recommended that the client do any necessary mixing itself so that only one IOProc is necessary. This routine has been deprecated in favor of AudioDeviceCreateIOProcID().

## Parameters

- `inDevice`: The AudioDevice to register the IOProc with.
- `inProc`: The AudioDeviceIOProc to register.
- `inClientData`: A pointer to client data that is passed back to the IOProc when it is called.

## See Also

### Deprecated Functions
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
- [AudioStreamAddPropertyListener](./audiostreamaddpropertylistener.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodeviceaddioproc)*