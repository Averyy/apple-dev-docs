# HandleChangeSampleRate

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the clock device the sample rate is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t HandleChangeSampleRate(double in_sample_rate);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

The default implementation calls [`SetSampleRate`](./setsamplerate.md) and returns [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md). Subclass and override this method to handle changes to the sample rate and return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) upon success.

## Parameters

- `in_sample_rate`: The sample rate to set, if possible, as a `double`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/handlechangesamplerate)*