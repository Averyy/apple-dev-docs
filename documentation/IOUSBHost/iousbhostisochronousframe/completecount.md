# completeCount

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The number of bytes that the system actually transferred for the frame.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+ - Deprecated in 27.0

## Declaration

```swift
var completeCount: UInt32
```

```c
uint32_t completeCount;
```

#### Discussion

[IOUSBHost](../IOUSBHost.md) updates this field upon completion of the frame.

## See Also

### Frame Structure
- [var status: IOReturn](./status.md)
  The completion status for an individual frame.
- [var requestCount: UInt32](./requestcount.md)
  The number of requested bytes to transfer for the frame.
- [var timeStamp: IOUSBHostTime](./timestamp.md)
  The observed time for the frame’s completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronousframe/completecount)*