# StartDevice

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the driver to start I/O on an audio device or audio clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t StartDevice(IOUserAudioObjectID in_object_id, IOUserAudioStartStopFlags in_flags);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The default implementation always returns [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md). Subclass and override this method to handle hardware-specific startup, then call the superclass to update the I/O state. The framework expects this call to always succeed for fail. The hardware can take as long as it needs in this call, provided it always either succeeds or fails.

This call results in a call to [`StartIO`](../iouseraudiodevice/startio.md) on the device.

## Parameters

- `in_object_id`: The identifier of the device on which to start I/O.
- `in_flags`: A flag that indicates how to perform the I/O start operation.

## See Also

### Starting and Stopping the Driver
- [StopDevice](./stopdevice.md)
  Tells the driver to stop I/O on an audio device or audio clock device.
- [IOUserAudioObjectID](../audiodriverkit-page/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [IOUserAudioStartStopFlags](../audiodriverkit-page/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/startdevice)*