# AudioServerPlugInHostInterface

**Framework**: Core Audio  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
struct AudioServerPlugInHostInterface;
```

## Topics

### Instance Properties
- [CopyFromStorage](./audioserverpluginhostinterface/copyfromstorage.md)
- [DeleteFromStorage](./audioserverpluginhostinterface/deletefromstorage.md)
- [PropertiesChanged](./audioserverpluginhostinterface/propertieschanged.md)
- [RequestDeviceConfigurationChange](./audioserverpluginhostinterface/requestdeviceconfigurationchange.md)
- [WriteToStorage](./audioserverpluginhostinterface/writetostorage.md)

## See Also

### Structures
- [AudioDriverPlugInHostInfo](./audiodriverpluginhostinfo.md)
- [struct AudioHardwareIOProcStreamUsage](./audiohardwareioprocstreamusage.md)
  This structure describes which streams a given AudioDeviceIOProc will use. It is used in conjunction with kAudioDevicePropertyIOProcStreamUsage.
- [struct AudioObjectPropertyAddress](./audioobjectpropertyaddress.md)
  An AudioObjectPropertyAddress collects the three parts that identify a specific property together in a struct for easy transmission.
- [AudioServerPlugInClientInfo](./audioserverpluginclientinfo.md)
- [AudioServerPlugInCustomPropertyInfo](./audioserverplugincustompropertyinfo.md)
- [AudioServerPlugInDriverInterface](./audioserverplugindriverinterface.md)
- [AudioServerPlugInIOCycleInfo](./audioserverpluginiocycleinfo.md)
- [struct AudioStreamRangedDescription](./audiostreamrangeddescription.md)
  This structure allows a specific sample rate range to be associated with an AudioStreamBasicDescription that specifies its sample rate as kAudioStreamAnyRate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverpluginhostinterface)*