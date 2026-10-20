# reserved

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+ - Deprecated in 27.0

## Declaration

```swift
var reserved: UInt32
```

```c
uint32_t reserved;
```

## See Also

### Instance Properties
- [var completeCount: UInt32](./completecount.md)
  The number of bytes that the system actually transferred for the frame.
- [var requestCount: UInt32](./requestcount.md)
  The number of requested bytes to transfer for the frame.
- [var status: IOReturn](./status.md)
  The completion status for an individual frame.
- [var timeStamp: IOUSBHostTime](./timestamp.md)
  The observed time for the frame’s completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronousframe/reserved)*