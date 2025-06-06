# requestCount

**Framework**: IOUSBHost  
**Kind**: property

The number of requested bytes to transfer for the frame.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var requestCount: UInt32
```

#### Discussion

> ❗ **Important**:  Initialize this field before submitting the structure.

 Initialize this field before submitting the structure.

## See Also

- [var status: IOReturn](iousbhostisochronousframe/status.md)
  The completion status for an individual frame.
- [var completeCount: UInt32](iousbhostisochronousframe/completecount.md)
  The number of bytes that the system actually transferred for the frame.
- [var timeStamp: IOUSBHostTime](iousbhostisochronousframe/timestamp.md)
  The observed time for the frame’s completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronousframe/requestcount)*