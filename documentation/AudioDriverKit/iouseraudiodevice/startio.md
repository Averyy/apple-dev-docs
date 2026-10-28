# StartIO

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the device to start I/O.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t StartIO(IOUserAudioStartStopFlags in_flags);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

The default implementation always returns [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md).

Subclass and override this method to handle hardware-specific tasks during I/O startup, then call the superclass to update the I/O state. The framework expects this call to always succeed or fail. The hardware can take as long as it needs in this call, provided it always either succeeds or fails.

All streams added to the device also receive a call to their [`StartIO`](../iouseraudiostream/startio.md) methods.

## Parameters

- `in_flags`: A `IOUserAudioStartStopFlag` to indicate I/O startup behavior.

## See Also

### Performing I/O
- [StopIO](./stopio.md)
  Tells the device to stop I/O.
- [IOUserAudioStartStopFlags](../audiodriverkit-page/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/startio)*