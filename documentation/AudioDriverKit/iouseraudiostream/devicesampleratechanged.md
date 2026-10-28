# DeviceSampleRateChanged

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Updates stream formats, in response to the owning audio device changing its sample rate.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t DeviceSampleRateChanged(double in_sample_rate);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

This method goes through all the available stream formats and selects the closet format with the matching sample rate.

Calling this method results in a call to the stream’s [`HandleChangeCurrentStreamFormat`](./handlechangecurrentstreamformat.md) to update its format.

## Parameters

- `in_sample_rate`: The new sample rate.

## See Also

### Supporting Sample Rate Changes
- [HandleChangeSampleRate](../iouseraudiodevice/handlechangesamplerate.md)
  Tells the device the sample rate is changing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/devicesampleratechanged)*