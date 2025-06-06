# StopIO

**Framework**: AudioDriverKit  
**Kind**: method

Tells the device to stop I/O.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t StopIO(IOUserAudioStartStopFlags in_flags);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation always returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess).

Subclass and override this method to handle hardware-specific tasks during I/O shutdown, then call the superclass to update the I/O state. The framework expects this call to always succeed or fail.

All streams added to the device also receive a call to their [`StopIO`](iouseraudiostream/stopio.md) methods.

## Parameters

- `in_flags`: A   to indicate I/O shutdown behavior.

## See Also

- [StartIO](iouseraudiodevice/startio.md)
  Tells the device to start I/O.
- [IOUserAudioStartStopFlags](audiodriverkit/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/stopio)*