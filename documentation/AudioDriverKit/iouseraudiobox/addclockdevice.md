# AddClockDevice

**Framework**: AudioDriverKit  
**Kind**: method

Adds an audio clock device to the audio box.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t AddClockDevice(IOUserAudioClockDevice * in_clock_device);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The box doesn’t own the clock device.

If adding the clock device succeeds, the clock device’s reference count increments by one.

## Parameters

- `in_clock_device`: The   to associate with the box.

## See Also

- [AddDevice](iouseraudiobox/adddevice.md)
  Adds an audio device to the audio box.
- [RemoveDevice](iouseraudiobox/removedevice.md)
  Removes an audio device from the audio box.
- [IOUserAudioDevice](iouseraudiodevice.md)
  An audio clock device object that handles the configurations for running I/O.
- [RemoveClockDevice](iouseraudiobox/removeclockdevice.md)
  Adds an audio clock device to the audio box.
- [IOUserAudioClockDevice](iouseraudioclockdevice.md)
  An audio clock device object, used to synchronize and perform I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/addclockdevice)*