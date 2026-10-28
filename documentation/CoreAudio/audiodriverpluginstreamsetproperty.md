# AudioDriverPlugInStreamSetProperty

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```c
extern OSStatus AudioDriverPlugInStreamSetProperty(AudioDeviceID inDevice, io_object_t inIOAudioStream, const AudioTimeStamp *inWhen, UInt32 inChannel, AudioDevicePropertyID inPropertyID, UInt32 inPropertyDataSize, const void *inPropertyData);
```

## Return Value

An OSStatus indicating success or failure. Note that if the plug-in does not implement the given property, it should return kAudioHardwareUnknownPropertyError to ensure that the HAL handles the property normally.

## Discussion

Tells the AudioStream object to change the value of the given property using the provided data.

Note that the value of the property should not be considered changed until the HAL has called the listeners as many properties values are changed asynchronously.

## Parameters

- `inDevice`: The AudioDevice whose stream is being changed.
- `inIOAudioStream`: The IOAudioStream to change.
- `inWhen`: A pointer to an AudioTimeStamp that says when to change the property’s value relative to the device’s time base. NULL means execute the change immediately.
- `inChannel`: The channel of the property to change where 0 is the main channel.
- `inPropertyID`: The AudioDevicePropertyID of the property to change.
- `inPropertyDataSize`: A UInt32 indicating the size of the buffer pointed to by inData.
- `inPropertyData`: The buffer containing the data to be used to change the property’s value.

## See Also

### Functions
- [func AudioConvertHostTimeToNanos(UInt64) -> UInt64](./audioconverthosttimetonanos%28_%29.md)
- [func AudioConvertNanosToHostTime(UInt64) -> UInt64](./audioconvertnanostohosttime%28_%29.md)
- [func AudioDeviceCreateIOProcID(AudioObjectID, AudioDeviceIOProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<AudioDeviceIOProcID?>) -> OSStatus](./audiodevicecreateioprocid%28_,_,_,_%29.md)
- [func AudioDeviceCreateIOProcIDWithBlock(UnsafeMutablePointer<AudioDeviceIOProcID?>, AudioObjectID, dispatch_queue_t?, AudioDeviceIOBlock) -> OSStatus](./audiodevicecreateioprocidwithblock%28_,_,_,_%29.md)
- [func AudioDeviceDestroyIOProcID(AudioObjectID, AudioDeviceIOProcID) -> OSStatus](./audiodevicedestroyioprocid%28_,_%29.md)
- [func AudioDeviceGetCurrentTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audiodevicegetcurrenttime%28_,_%29.md)
- [func AudioDeviceGetNearestStartTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](./audiodevicegetneareststarttime%28_,_,_%29.md)
- [func AudioDeviceStart(AudioObjectID, AudioDeviceIOProcID?) -> OSStatus](./audiodevicestart%28_,_%29.md)
- [func AudioDeviceStartAtTime(AudioObjectID, AudioDeviceIOProcID?, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](./audiodevicestartattime%28_,_,_,_%29.md)
- [func AudioDeviceStop(AudioObjectID, AudioDeviceIOProcID?) -> OSStatus](./audiodevicestop%28_,_%29.md)
- [func AudioDeviceTranslateTime(AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audiodevicetranslatetime%28_,_,_%29.md)
- [AudioDriverPlugInClose](./audiodriverpluginclose.md)
- [AudioDriverPlugInDeviceGetProperty](./audiodriverplugindevicegetproperty.md)
- [AudioDriverPlugInDeviceGetPropertyInfo](./audiodriverplugindevicegetpropertyinfo.md)
- [AudioDriverPlugInDeviceSetProperty](./audiodriverplugindevicesetproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodriverpluginstreamsetproperty)*