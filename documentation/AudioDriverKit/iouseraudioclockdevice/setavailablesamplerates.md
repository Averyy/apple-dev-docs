# SetAvailableSampleRates

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the available sample rates for the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetAvailableSampleRates(const double *in_sample_rates, size_t in_num_rates);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

If successful, changing the available sample rates sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_sample_rates`: A pointer to a buffer of `double` values containing the available sample rates.
- `in_num_rates`: The number of sample rates in `in_sample_rates` buffer.

## See Also

### Working with Sample Rates
- [SetSampleRate](./setsamplerate.md)
  Sets the sample rate for the clock device.
- [GetSampleRate](./getsamplerate.md)
  Gets the sample rate of the clock device.
- [GetAvailableSampleRates](./getavailablesamplerates.md)
  Gets the available sample rates of the clock device.
- [GetNumberAvailableSampleRates](./getnumberavailablesamplerates.md)
  Gets the number of available sample rates of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setavailablesamplerates)*