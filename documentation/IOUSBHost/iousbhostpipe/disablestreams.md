# disableStreams()

**Framework**: IOUSBHost  
**Kind**: method

Disables streams for the pipe.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func disableStreams() throws
```

#### Discussion

This method changes the operational mode of the [`IOUSBHostPipe`](https://developer.apple.com/documentation/kernel/iousbhostpipe) to disable streaming endpoint transfers. Before calling this method, set all stream contexts as nonactive on the device through an out-of-band (class-defined) mechanism, in accordance with USB 3.2, 8.12.1.4. This is necessary, as the method synchronously aborts any outstanding calls on existing [`IOUSBHostStream`](iousbhoststream.md) objects.

## See Also

- [func enableStreams() throws](iousbhostpipe/enablestreams.md)
  Enables streams for the pipe.
- [func copyStream(withStreamID: Int) throws -> IOUSBHostStream](iousbhostpipe/copystream(withstreamid:).md)
  Returns the stream for a stream ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/disablestreams())*