# EndIOOperation

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, unsigned int, unsigned int, unsigned int, const struct AudioServerPlugInIOCycleInfo *) __attribute__((nonblocking)) EndIOOperation;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Tells the plug-in that the Host is about to end a phase of the IO cycle for a particular device.

## Parameters

- `inDriver`: The plug-in that owns the device.
- `inDeviceObjectID`: The ID of the device.
- `inClientID`: The ID of the client doing the operation. This will have been established with the device by a previous call to AddDeviceClient().
- `inOperationID`: A UInt32 that identifies the operation being performed. Constants for the valid values of this argument are listed in the Constants section.
- `inIOBufferFrameSize`: The number of sample frames that will be processed in this operation. Note that for some operations, this will be different than the nominal buffer frame size.
- `inIOCycleInfo`: The basic information about the current IO cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/endiooperation)*