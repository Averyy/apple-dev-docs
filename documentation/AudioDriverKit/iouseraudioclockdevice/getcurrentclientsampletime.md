# GetCurrentClientSampleTime

**Framework**: AudioDriverKit  
**Kind**: method

Gets the current sample time in the ring buffer that the client has written to or read from.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
void GetCurrentClientSampleTime(uint64_t * out_input_sample_time, uint64_t * out_output_sample_time);
```

## Parameters

- `out_input_sample_time`: On return, the current input sample time read by the client.
- `out_output_sample_time`: On return, the current output sample time written by the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getcurrentclientsampletime)*