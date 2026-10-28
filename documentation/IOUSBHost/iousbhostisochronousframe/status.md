# status

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The completion status for an individual frame.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+ - Deprecated in 27.0

## Declaration

```swift
var status: IOReturn
```

```c
IOReturn status;
```

## Discussion

[IOUSBHost](../IOUSBHost.md) initializes this to [`kIOReturnInvalid`](../../iokit/kioreturninvalid.md) and updates the field with a valid status code upon completion of the frame.

## See Also

### Frame Structure
- [var requestCount: UInt32](./requestcount.md)
  The number of requested bytes to transfer for the frame.
- [var completeCount: UInt32](./completecount.md)
  The number of bytes that the system actually transferred for the frame.
- [var timeStamp: IOUSBHostTime](./timestamp.md)
  The observed time for the frame’s completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronousframe/status)*