# AudioStreamGetPropertyInfo

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.1+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus AudioStreamGetPropertyInfo(AudioStreamID inStream, UInt32 inChannel, AudioDevicePropertyID inPropertyID, UInt32 *outSize, Boolean *outWritable);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Retrieve information about the given property of an AudioStream.

## Parameters

- `inStream`: The AudioStream to query.
- `inChannel`: The channel of the property to query where 0 is the main channel.
- `inPropertyID`: The AudioDevicePropertyID of the property to query.
- `outSize`: A pointer to a UInt32 that receives the size of the property data in bytes on exit. This can be NULL if the size information is not being requested.
- `outWritable`: A pointer to a Boolean that receives indication of whether or not the given property can be set. This can be NULL if the writability is not being requested.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiostreamgetpropertyinfo)*