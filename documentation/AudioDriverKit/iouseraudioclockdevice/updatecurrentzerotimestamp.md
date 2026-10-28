# UpdateCurrentZeroTimestamp

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Updates the current timestamp value.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
void UpdateCurrentZeroTimestamp(uint64_t in_sample_time, uint64_t in_host_time);
```

## Discussion

Updating the current timestamp should use the time passed in the hardware interrupt.

## Parameters

- `in_sample_time`: The most current sample time tracked by the hardware device.
- `in_host_time`: The most current host time tracked by the hardware device.

## See Also

### Accessing Timestamps
- [GetCurrentZeroTimestamp](./getcurrentzerotimestamp.md)
  Gets the current zero timestamp value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/updatecurrentzerotimestamp)*