# AudioHardwareAddRunLoopSource

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.3+ - Deprecated in 10.7

## Declaration

```c
extern OSStatus AudioHardwareAddRunLoopSource(CFRunLoopSourceRef inRunLoopSource);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Add the given CFRunLoopSource to the the HAL’s notification CFRunLoop.

The CFRunLoop the HAL uses for notifications is specified by kAudioHardwarePropertyRunLoop. If kAudioHardwarePropertyRunLoop changes, CFRunLoopSources added with this function will automatically be transferred to the new CFRunLoop. Usage of the HAL’s notification run loop is deprecated. Please use libdispatch instead.

## Parameters

- `inRunLoopSource`: The CFRunLoopSource to add.

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
- [AudioHardwareGetProperty](./audiohardwaregetproperty.md)
- [AudioHardwareGetPropertyInfo](./audiohardwaregetpropertyinfo.md)
- [AudioHardwareRemovePropertyListener](./audiohardwareremovepropertylistener.md)
- [AudioHardwareRemoveRunLoopSource](./audiohardwareremoverunloopsource.md)
- [AudioHardwareSetProperty](./audiohardwaresetproperty.md)
- [AudioStreamAddPropertyListener](./audiostreamaddpropertylistener.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareaddrunloopsource)*