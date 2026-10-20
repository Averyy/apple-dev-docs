# IOUSBHostTime

**Framework**: IOUSBHost  
**Kind**: typealias  
**Role**: Type Alias

The absolute time.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias IOUSBHostTime = UInt64
```

```c
typedef uint64_t IOUSBHostTime;
```

## See Also

### Sending Isochronous I/O
- [typealias IOUSBHostIsochronousCompletionHandler](./iousbhostisochronouscompletionhandler.md)
  A completion handler for asynchronous isochronous transfers.
- [struct IOUSBHostIsochronousFrame](./iousbhostisochronousframe.md)
  A structure that represents a single frame in an isochronous transfer.
- [func enqueueIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousFrame>) -> Void)?) throws](./iousbhostpipe/enqueueiorequest%28with,framelist,framelistcount,firstframenumber,completionhandler%29.md)
  Enqueues a request on an isochronous endpoint.
- [func sendIORequest(with: NSMutableData, frameList: UnsafeMutablePointer<IOUSBHostIsochronousFrame>, frameListCount: Int, firstFrameNumber: UInt64) throws](./iousbhostpipe/sendiorequest%28with,framelist,framelistcount,firstframenumber%29.md)
  Sends a request on an isochronous endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhosttime)*