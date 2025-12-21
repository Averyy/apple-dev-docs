# streams

**Framework**: Core Audio  
**Kind**: property

An array of AudioHardwareStreams that represent the IO streams of the device.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var streams: [AudioHardwareStream] { get throws }
```

#### Discussion

If a notification is received for this property, any cached stream objects for the device become invalid and need to be re-fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/streams)*