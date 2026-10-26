# RequestDeviceConfigurationChange

**Framework**: Core Audio  
**Kind**: property  
**Role**: Instance Property

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
int (*)(const struct AudioServerPlugInHostInterface *, unsigned int, unsigned long long, void *) RequestDeviceConfigurationChange;
```

#### Return Value

An OSStatus indicating success or failure. Note that even if this method indicates success, the Host may still abort the change later.

#### Discussion

Plug-ins invoke this routine to tell the Host to initiate a configuration change operation.

When a plug-in’s device object needs to change its structure or change any state related to IO for any reason, it must begin this operation by invoking this Host method. The device object may not perform the state change until the Host gives the device clearance to do so by invoking the plug-in’s PerformDeviceConfigurationChange() routine. Note that the call to PerformDeviceConfigurationChange() may be deferred to another thread at the discretion of the host. The sorts of changes that must go through this mechanism are anything that affects either the structure of the device or IO. This includes, but is not limited to, changing stream layout, adding/removing controls, changing the nominal sample rate of the device, changing any sample formats on any stream on the device, changing the size of the ring buffer, changing presentation latency, and changing the safety offset.

## Parameters

- `inHost`: The AudioServerPlugInHostRef passed to the plug-in at initialization.
- `inDeviceObjectID`: The AudioObjectID of the device making the request.
- `inChangeAction`: A UInt64 indicating the action the device object wants to take. It will be passed back to the device in the invocation of PerformDeviceConfigurationChange(). Note that this value is purely for the plug-in’s usage. The Host does not look at this value.
- `inChangeInfo`: A pointer to information about the configuration change. It will be passed back to the device in the invocation of PerformDeviceConfigurationChange(). Note that this value is purely for the plug-in’s usage. The Host does not look at this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverpluginhostinterface/requestdeviceconfigurationchange)*