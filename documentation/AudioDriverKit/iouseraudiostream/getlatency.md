# GetLatency

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 21.0+

## Declaration

```c
uint32_t GetLatency();
```

#### Return Value

Returns uint32_t

#### Discussion

Get the latency of the stream in sample frames.

Getting the value will be synchronized using the work queue created by the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/getlatency)*