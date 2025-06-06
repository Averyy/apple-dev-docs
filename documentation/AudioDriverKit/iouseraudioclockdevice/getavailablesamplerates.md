# GetAvailableSampleRates

**Framework**: AudioDriverKit  
**Kind**: method

Gets the available sample rates of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
size_t GetAvailableSampleRates(double * out_sample_rates, size_t in_num_rates);
```

#### Return Value

A `size_t` that indicates how many rates were set in the `out_sample_rates` buffer.

#### Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `out_sample_rates`: A pointer to a buffer of type   whose size corresponds to  . After the call completes, this buffer contains the available sample rates.
- `in_num_rates`: The number of rates in the   buffer.

## See Also

- [SetSampleRate](iouseraudioclockdevice/setsamplerate.md)
  Sets the sample rate for the clock device.
- [GetSampleRate](iouseraudioclockdevice/getsamplerate.md)
  Gets the sample rate of the clock device.
- [SetAvailableSampleRates](iouseraudioclockdevice/setavailablesamplerates.md)
  Sets the available sample rates for the clock device.
- [GetNumberAvailableSampleRates](iouseraudioclockdevice/getnumberavailablesamplerates.md)
  Gets the number of available sample rates of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getavailablesamplerates)*