# AudioDriverPlugInStreamGetProperty

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```c
extern OSStatus AudioDriverPlugInStreamGetProperty(AudioDeviceID inDevice, io_object_t inIOAudioStream, UInt32 inChannel, AudioDevicePropertyID inPropertyID, UInt32 *ioPropertyDataSize, void *outPropertyData);
```

#### Return Value

An OSStatus indicating success or failure. Note that if the plug-in does not implement the given property, it should return kAudioHardwareUnknownPropertyError to ensure that the HAL handles the property normally.

#### Discussion

Queries an the AudioStream object to get the data of the given property and places it in the provided buffer.

## Parameters

- `inDevice`: The AudioDevice whose stream is being queried.
- `inIOAudioStream`: The IOAudioStream to query.
- `inChannel`: The channel of the property to query where 0 is the main channel.
- `inPropertyID`: The AudioDevicePropertyID of the property to query.
- `ioPropertyDataSize`: A UInt32 which on entry indicates the size of the buffer pointed to by outData and on exit indicates how much of the buffer was used.
- `outPropertyData`: The buffer into which the object will put the data for the given property.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodriverpluginstreamgetproperty)*