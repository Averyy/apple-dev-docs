# AudioStreamSetProperty

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.1+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus AudioStreamSetProperty(AudioStreamID inStream, const AudioTimeStamp *inWhen, UInt32 inChannel, AudioDevicePropertyID inPropertyID, UInt32 inPropertyDataSize, const void *inPropertyData);
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Tells the AudioStream object to change the value of the given property using the provided data.

Note that the value of the property should not be considered changed until the HAL has called the listeners as many properties values are changed asynchronously. Also note that the same functionality is provided by the function AudioObjectSetPropertyData().

## Parameters

- `inStream`: The AudioStream to change.
- `inWhen`: A pointer to an AudioTimeStamp that says when to change the property’s value relative to the device’s time base. NULL means execute the change immediately.
- `inChannel`: The channel of the property to change where 0 is the main channel.
- `inPropertyID`: The AudioDevicePropertyID of the property to change.
- `inPropertyDataSize`: A UInt32 indicating the size of the buffer pointed to by inData.
- `inPropertyData`: The buffer containing the data to be used to change the property’s value.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiostreamsetproperty)*