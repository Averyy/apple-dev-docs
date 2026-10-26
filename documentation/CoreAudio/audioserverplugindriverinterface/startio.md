# StartIO

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, unsigned int) StartIO;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Tells the device to start IO.

This call is expect to always succeed or fail. The hardware can take as long as necessary in this call such that it always either succeeds (and returns 0) or fails.

## Parameters

- `inDriver`: The plug-in that owns the device.
- `inDeviceObjectID`: The device to start.
- `inClientID`: The ID of the client making the request. This will have been established with the device by a previous call to AddDeviceClient(). Note that the device should consider IO running for as long as at least one client has started IO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/startio)*