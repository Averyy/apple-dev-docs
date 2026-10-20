# RemoveClockDevice

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds an audio clock device to the audio box.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t RemoveClockDevice(IOUserAudioClockDevice *in_clock_device);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If removing the clock device succeeds, the clock device’s reference count decrements by one.

## Parameters

- `in_clock_device`: The [`IOUserAudioClockDevice`](../iouseraudioclockdevice.md) to disassociate from the box.

## See Also

### Managing Box Contents
- [AddDevice](./adddevice.md)
  Adds an audio device to the audio box.
- [RemoveDevice](./removedevice.md)
  Removes an audio device from the audio box.
- [IOUserAudioDevice](../iouseraudiodevice.md)
  An audio clock device object that handles the configurations for running I/O.
- [AddClockDevice](./addclockdevice.md)
  Adds an audio clock device to the audio box.
- [IOUserAudioClockDevice](../iouseraudioclockdevice.md)
  An audio clock device object, used to synchronize and perform I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/removeclockdevice)*