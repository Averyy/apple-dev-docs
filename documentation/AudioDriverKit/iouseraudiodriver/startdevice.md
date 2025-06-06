# StartDevice

**Framework**: AudioDriverKit  
**Kind**: method

Tells the driver to start I/O on an audio device or audio clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t StartDevice(IOUserAudioObjectID in_object_id, IOUserAudioStartStopFlags in_flags);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation always returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess). Subclass and override this method to handle hardware-specific startup, then call the superclass to update the I/O state. The framework expects this call to always succeed for fail. The hardware can take as long as it needs in this call, provided it always either succeeds or fails.

This call results in a call to [`StartIO`](iouseraudiodevice/startio.md) on the device.

## Parameters

- `in_object_id`: The identifier of the device on which to start I/O.
- `in_flags`: A flag that indicates how to perform the I/O start operation.

## See Also

- [StopDevice](iouseraudiodriver/stopdevice.md)
  Tells the driver to stop I/O on an audio device or audio clock device.
- [IOUserAudioObjectID](audiodriverkit/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [IOUserAudioStartStopFlags](audiodriverkit/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/startdevice)*