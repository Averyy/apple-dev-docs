# GetCurrentZeroTimestamp

**Framework**: AudioDriverKit  
**Kind**: method

Gets the current zero timestamp value.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
void GetCurrentZeroTimestamp(uint64_t * out_sample_time, uint64_t * out_host_time);
```

## Parameters

- `out_sample_time`: On return, the most current sample time tracked by the hardware device.
- `out_host_time`: On return, the most current host time tracked by the hardware device.

## See Also

- [UpdateCurrentZeroTimestamp](iouseraudioclockdevice/updatecurrentzerotimestamp.md)
  Updates the current timestamp value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getcurrentzerotimestamp)*