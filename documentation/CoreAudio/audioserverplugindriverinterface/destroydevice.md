# DestroyDevice

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int) DestroyDevice;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Called to tell the plug-in about to destroy the given device.

## Parameters

- `inDriver`: The plug-in that owns the device.
- `inDeviceObjectID`: The ID of the device to destroy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/destroydevice)*