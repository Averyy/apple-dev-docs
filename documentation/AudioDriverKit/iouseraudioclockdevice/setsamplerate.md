# SetSampleRate

**Framework**: AudioDriverKit  
**Kind**: method

Sets the sample rate for the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetSampleRate(double in_sample_rate);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the sample rate sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_sample_rate`: The sample rate to set on the clock device.

## See Also

- [GetSampleRate](iouseraudioclockdevice/getsamplerate.md)
  Gets the sample rate of the clock device.
- [SetAvailableSampleRates](iouseraudioclockdevice/setavailablesamplerates.md)
  Sets the available sample rates for the clock device.
- [GetAvailableSampleRates](iouseraudioclockdevice/getavailablesamplerates.md)
  Gets the available sample rates of the clock device.
- [GetNumberAvailableSampleRates](iouseraudioclockdevice/getnumberavailablesamplerates.md)
  Gets the number of available sample rates of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setsamplerate)*