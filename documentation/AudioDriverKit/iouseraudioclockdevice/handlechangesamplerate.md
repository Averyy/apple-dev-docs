# HandleChangeSampleRate

**Framework**: AudioDriverKit  
**Kind**: method

Tells the clock device the sample rate is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
virtual kern_return_t HandleChangeSampleRate(double in_sample_rate);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

#### Discussion

The default implementation calls [`SetSampleRate`](iouseraudioclockdevice/setsamplerate.md) and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess). Subclass and override this method to handle changes to the sample rate and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) upon success.

## Parameters

- `in_sample_rate`: The sample rate to set, if possible, as a `double`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/handlechangesamplerate)*