# RemoveDevice

**Framework**: AudioDriverKit  
**Kind**: method

Removes an audio device from the audio box.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t RemoveDevice(IOUserAudioDevice * in_device);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If removing the device succeeds, the device’s reference count decrements by one.

## Parameters

- `in_device`: The   to disassociate from the box.

## See Also

- [AddDevice](iouseraudiobox/adddevice.md)
  Adds an audio device to the audio box.
- [IOUserAudioDevice](iouseraudiodevice.md)
  An audio clock device object that handles the configurations for running I/O.
- [AddClockDevice](iouseraudiobox/addclockdevice.md)
  Adds an audio clock device to the audio box.
- [RemoveClockDevice](iouseraudiobox/removeclockdevice.md)
  Adds an audio clock device to the audio box.
- [IOUserAudioClockDevice](iouseraudioclockdevice.md)
  An audio clock device object, used to synchronize and perform I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/removedevice)*