# AudioServerPlugInDriverInterface

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
struct AudioServerPlugInDriverInterface;
```

## Topics

### Instance Properties
- [AbortDeviceConfigurationChange](./audioserverplugindriverinterface/abortdeviceconfigurationchange.md)
- [AddDeviceClient](./audioserverplugindriverinterface/adddeviceclient.md)
- [AddRef](./audioserverplugindriverinterface/addref.md)
- [BeginIOOperation](./audioserverplugindriverinterface/beginiooperation.md)
- [CreateDevice](./audioserverplugindriverinterface/createdevice.md)
- [DestroyDevice](./audioserverplugindriverinterface/destroydevice.md)
- [DoIOOperation](./audioserverplugindriverinterface/doiooperation.md)
- [EndIOOperation](./audioserverplugindriverinterface/endiooperation.md)
- [GetPropertyData](./audioserverplugindriverinterface/getpropertydata.md)
- [GetPropertyDataSize](./audioserverplugindriverinterface/getpropertydatasize.md)
- [GetZeroTimeStamp](./audioserverplugindriverinterface/getzerotimestamp.md)
- [HasProperty](./audioserverplugindriverinterface/hasproperty.md)
- [Initialize](./audioserverplugindriverinterface/initialize.md)
- [IsPropertySettable](./audioserverplugindriverinterface/ispropertysettable.md)
- [PerformDeviceConfigurationChange](./audioserverplugindriverinterface/performdeviceconfigurationchange.md)
- [QueryInterface](./audioserverplugindriverinterface/queryinterface.md)
- [Release](./audioserverplugindriverinterface/release.md)
- [RemoveDeviceClient](./audioserverplugindriverinterface/removedeviceclient.md)
- [SetPropertyData](./audioserverplugindriverinterface/setpropertydata.md)
- [StartIO](./audioserverplugindriverinterface/startio.md)
- [StopIO](./audioserverplugindriverinterface/stopio.md)
- [WillDoIOOperation](./audioserverplugindriverinterface/willdoiooperation.md)

## See Also

### Structures
- [AudioDriverPlugInHostInfo](./audiodriverpluginhostinfo.md)
- [struct AudioHardwareIOProcStreamUsage](./audiohardwareioprocstreamusage.md)
  This structure describes which streams a given AudioDeviceIOProc will use. It is used in conjunction with kAudioDevicePropertyIOProcStreamUsage.
- [struct AudioObjectPropertyAddress](./audioobjectpropertyaddress.md)
  An AudioObjectPropertyAddress collects the three parts that identify a specific property together in a struct for easy transmission.
- [AudioServerPlugInClientInfo](./audioserverpluginclientinfo.md)
- [AudioServerPlugInCustomPropertyInfo](./audioserverplugincustompropertyinfo.md)
- [AudioServerPlugInHostInterface](./audioserverpluginhostinterface.md)
- [AudioServerPlugInIOCycleInfo](./audioserverpluginiocycleinfo.md)
- [struct AudioStreamRangedDescription](./audiostreamrangeddescription.md)
  This structure allows a specific sample rate range to be associated with an AudioStreamBasicDescription that specifies its sample rate as kAudioStreamAnyRate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface)*