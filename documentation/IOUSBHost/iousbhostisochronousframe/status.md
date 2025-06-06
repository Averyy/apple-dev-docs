# status

**Framework**: IOUSBHost  
**Kind**: property

The completion status for an individual frame.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var status: IOReturn
```

#### Discussion

[`IOUSBHost`](IOUSBHost.md) initializes this to [`kIOReturnInvalid`](https://developer.apple.com/documentation/iokit/kioreturninvalid) and updates the field with a valid status code upon completion of the frame.

## See Also

- [var requestCount: UInt32](iousbhostisochronousframe/requestcount.md)
  The number of requested bytes to transfer for the frame.
- [var completeCount: UInt32](iousbhostisochronousframe/completecount.md)
  The number of bytes that the system actually transferred for the frame.
- [var timeStamp: IOUSBHostTime](iousbhostisochronousframe/timestamp.md)
  The observed time for the frame’s completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronousframe/status)*