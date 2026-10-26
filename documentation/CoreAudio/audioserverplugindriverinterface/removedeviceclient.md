# RemoveDeviceClient

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, const struct AudioServerPlugInClientInfo *) RemoveDeviceClient;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Called to tell the plug-in about a client that is no longer using the device.

## Parameters

- `inDriver`: The plug-in that owns the device.
- `inDeviceObjectID`: The ID of the device that the client is no longer using.
- `inClientInfo`: A pointer to an AudioServerPlugInClientInfo structure describing the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/removedeviceclient)*