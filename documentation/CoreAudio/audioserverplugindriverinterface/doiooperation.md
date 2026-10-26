# DoIOOperation

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
int (*)(struct AudioServerPlugInDriverInterface **, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, const struct AudioServerPlugInIOCycleInfo *, void *, void *) __attribute__((nonblocking)) DoIOOperation;
```

#### Return Value

An OSStatus indicating success or failure.

#### Discussion

Tells the device to perform an IO operation for a particular stream.

## Parameters

- `inDriver`: The plug-in that owns the device.
- `inDeviceObjectID`: The ID of the device.
- `inStreamObjectID`: The ID of the stream whose data is being processed.
- `inClientID`: The ID of the client doing the operation. This will have been established with the device by a previous call to AddDeviceClient().
- `inOperationID`: A UInt32 that identifies the operation being performed. Constants for the valid values of this argument are listed in the Constants section.
- `inIOBufferFrameSize`: The number of sample frames that will be processed in this operation. Note that for some operations, this will be different than the nominal buffer frame size.
- `inIOCycleInfo`: The basic information about the current IO cycle.
- `ioMainBuffer`: The primary buffer for the data for the operation. If the device signaled through WillDoIOOperation() that the operation will be handled in-place, this will be the only buffer passed in.
- `ioSecondaryBuffer`: The secondary buffer for performing the operation. If the device signaled through WillDoIOOperation() that the operation will not be handled in place, the results of the operation must end up in this buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/doiooperation)*