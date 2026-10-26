# AudioDriverPlugInHostInfo

**Framework**: Core Audio  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```c
struct AudioDriverPlugInHostInfo;
```

## Topics

### Instance Properties
- [mDeviceID](./audiodriverpluginhostinfo/mdeviceid.md)
- [mDevicePropertyChangedProc](./audiodriverpluginhostinfo/mdevicepropertychangedproc.md)
- [mIOAudioDevice](./audiodriverpluginhostinfo/mioaudiodevice.md)
- [mIOAudioEngine](./audiodriverpluginhostinfo/mioaudioengine.md)
- [mStreamPropertyChangedProc](./audiodriverpluginhostinfo/mstreampropertychangedproc.md)

## See Also

### Structures
- [struct AudioHardwareIOProcStreamUsage](./audiohardwareioprocstreamusage.md)
  This structure describes which streams a given AudioDeviceIOProc will use. It is used in conjunction with kAudioDevicePropertyIOProcStreamUsage.
- [struct AudioObjectPropertyAddress](./audioobjectpropertyaddress.md)
  An AudioObjectPropertyAddress collects the three parts that identify a specific property together in a struct for easy transmission.
- [AudioServerPlugInClientInfo](./audioserverpluginclientinfo.md)
- [AudioServerPlugInCustomPropertyInfo](./audioserverplugincustompropertyinfo.md)
- [AudioServerPlugInDriverInterface](./audioserverplugindriverinterface.md)
- [AudioServerPlugInHostInterface](./audioserverpluginhostinterface.md)
- [AudioServerPlugInIOCycleInfo](./audioserverpluginiocycleinfo.md)
- [struct AudioStreamRangedDescription](./audiostreamrangeddescription.md)
  This structure allows a specific sample rate range to be associated with an AudioStreamBasicDescription that specifies its sample rate as kAudioStreamAnyRate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodriverpluginhostinfo)*