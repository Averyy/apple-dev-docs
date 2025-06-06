# GetNumberAvailableSampleRates

**Framework**: AudioDriverKit  
**Kind**: method

Gets the number of available sample rates of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
size_t GetNumberAvailableSampleRates();
```

#### Return Value

The number of available sample rates of the clock device.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetSampleRate](iouseraudioclockdevice/setsamplerate.md)
  Sets the sample rate for the clock device.
- [GetSampleRate](iouseraudioclockdevice/getsamplerate.md)
  Gets the sample rate of the clock device.
- [SetAvailableSampleRates](iouseraudioclockdevice/setavailablesamplerates.md)
  Sets the available sample rates for the clock device.
- [GetAvailableSampleRates](iouseraudioclockdevice/getavailablesamplerates.md)
  Gets the available sample rates of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getnumberavailablesamplerates)*