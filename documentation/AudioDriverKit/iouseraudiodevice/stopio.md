# StopIO

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the device to stop I/O.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t StopIO(IOUserAudioStartStopFlags in_flags);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

The default implementation always returns [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md).

Subclass and override this method to handle hardware-specific tasks during I/O shutdown, then call the superclass to update the I/O state. The framework expects this call to always succeed or fail.

All streams added to the device also receive a call to their [`StopIO`](../iouseraudiostream/stopio.md) methods.

## Parameters

- `in_flags`: A `IOUserAudioStartStopFlag` to indicate I/O shutdown behavior.

## See Also

### Performing I/O
- [StartIO](./startio.md)
  Tells the device to start I/O.
- [IOUserAudioStartStopFlags](../audiodriverkit-page/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/stopio)*