# StopIO

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, unsigned int) StopIO;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Tells the device to stop IO.

## Parameters

- `inDriver`: The plug-in that owns the device.
- `inDeviceObjectID`: The device to stop.
- `inClientID`: The ID of the client making the request. This will have been established with the device by a previous call to AddDeviceClient().


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/stopio)*