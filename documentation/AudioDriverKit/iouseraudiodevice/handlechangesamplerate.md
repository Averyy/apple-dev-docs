# HandleChangeSampleRate

**Framework**: AudioDriverKit  
**Kind**: method

Tells the device the sample rate is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t HandleChangeSampleRate(double in_sample_rate);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation calls [`SetSampleRate`](iouseraudioclockdevice/setsamplerate.md) and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess). Subclass and override this method to handle changes to the sample rate and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) upon success.

## Parameters

- `in_sample_rate`: The sample rate to set, if possible, as a  .

## See Also

- [DeviceSampleRateChanged](iouseraudiostream/devicesampleratechanged.md)
  Updates stream formats, in response to the owning audio device changing its sample rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/handlechangesamplerate)*