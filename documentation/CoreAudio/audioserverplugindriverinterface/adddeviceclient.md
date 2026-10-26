# AddDeviceClient

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, const struct AudioServerPlugInClientInfo *) AddDeviceClient;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Called to tell the plug-in about a new client of the Host for a particular device.

## Parameters

- `inDriver`: The plug-in that owns the device.
- `inDeviceObjectID`: The ID of the device that the client is using.
- `inClientInfo`: A pointer to an AudioServerPlugInClientInfo structure describing the new client. The plug-in should cache this data (including taking a retain on the bundle ID) as the memory pointed is only valid for the duration of the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/adddeviceclient)*