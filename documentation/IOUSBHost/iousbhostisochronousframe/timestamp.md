# timeStamp

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The observed time for the frame’s completion.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+ - Deprecated in 27.0

## Declaration

```swift
var timeStamp: IOUSBHostTime
```

```c
IOUSBHostTime timeStamp;
```

## Discussion

> **Note**:  Interrupt latency and system load may result in more than one frame completing with the same timestamp.

## See Also

### Frame Structure
- [var status: IOReturn](./status.md)
  The completion status for an individual frame.
- [var requestCount: UInt32](./requestcount.md)
  The number of requested bytes to transfer for the frame.
- [var completeCount: UInt32](./completecount.md)
  The number of bytes that the system actually transferred for the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronousframe/timestamp)*