# AddDevice

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds an audio device to the audio box.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t AddDevice(IOUserAudioDevice *in_device);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The box doesn’t own the device.

If adding the device succeeds, the device’s reference count increments by one.

## Parameters

- `in_device`: The [`IOUserAudioDevice`](../iouseraudiodevice.md) to associate with the box.

## See Also

### Managing Box Contents
- [RemoveDevice](./removedevice.md)
  Removes an audio device from the audio box.
- [IOUserAudioDevice](../iouseraudiodevice.md)
  An audio clock device object that handles the configurations for running I/O.
- [AddClockDevice](./addclockdevice.md)
  Adds an audio clock device to the audio box.
- [RemoveClockDevice](./removeclockdevice.md)
  Adds an audio clock device to the audio box.
- [IOUserAudioClockDevice](../iouseraudioclockdevice.md)
  An audio clock device object, used to synchronize and perform I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/adddevice)*