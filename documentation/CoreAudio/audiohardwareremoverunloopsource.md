# AudioHardwareRemoveRunLoopSource

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.3+ - Deprecated in 10.7

## Declaration

```c
extern OSStatus AudioHardwareRemoveRunLoopSource(CFRunLoopSourceRef inRunLoopSource);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Remove the given CFRunLoopSource from the the HAL’s notification CFRunLoop.

The CFRunLoop the HAL uses for notifications is specified by kAudioHardwarePropertyRunLoop. Usage of the HAL’s notification run loop is deprecated. Please use libdispatch instead.

## Parameters

- `inRunLoopSource`: The CFRunLoopSource to remove.

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
- [AudioHardwareSetProperty](./audiohardwaresetproperty.md)
- [AudioStreamAddPropertyListener](./audiostreamaddpropertylistener.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareremoverunloopsource)*