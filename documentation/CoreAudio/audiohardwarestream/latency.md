# latency

**Framework**: Core Audio  
**Kind**: property

An Int containing the number of frames of latency in the stream.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var latency: Int { get throws }
```

#### Discussion

Note that the owning device may have additional latency so it should be queried as well. If both the device and the stream say they have latency, then the total latency for the stream is the device latency summed with the stream latency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarestream/latency)*