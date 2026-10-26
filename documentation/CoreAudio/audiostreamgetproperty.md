# AudioStreamGetProperty

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.1+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus AudioStreamGetProperty(AudioStreamID inStream, UInt32 inChannel, AudioDevicePropertyID inPropertyID, UInt32 *ioPropertyDataSize, void *outPropertyData);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Queries an the AudioStream object to get the data of the given property and places it in the provided buffer.

Note that the same functionality is provided by the function AudioObjectGetPropertyData().

## Parameters

- `inStream`: The AudioStream to query.
- `inChannel`: The channel of the property to query where 0 is the main channel.
- `inPropertyID`: The AudioDevicePropertyID of the property to query.
- `ioPropertyDataSize`: A UInt32 which on entry indicates the size of the buffer pointed to by outData and on exit indicates how much of the buffer was used.
- `outPropertyData`: The buffer into which the object will put the data for the given property.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiostreamgetproperty)*