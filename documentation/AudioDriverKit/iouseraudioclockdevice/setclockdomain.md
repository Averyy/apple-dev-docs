# SetClockDomain

**Framework**: AudioDriverKit  
**Kind**: method

Sets the clock domain value of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetClockDomain(uint32_t in_clock_domain);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Drivers can change the transport type of the clock device dynamically. If successful, changing the transport type sends a notification to the host to update the object state.

## Parameters

- `in_clock_domain`: The clock domain to set, as a  . This value indicates the clock domain to which this AudioDevice belongs. Audio hardware can synchronize AudioDevices that have the same value for this property. However, a value of   indicates an unspecified clock domain for the device. The framework assumes devices with unspecified clock domains are separate from one another, even if they also has   as their clock domain value.

## See Also

- [GetClockDomain](iouseraudioclockdevice/getclockdomain.md)
  Gets the clock domain value of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setclockdomain)*