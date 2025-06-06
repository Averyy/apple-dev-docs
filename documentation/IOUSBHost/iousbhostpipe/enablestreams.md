# enableStreams()

**Framework**: IOUSBHost  
**Kind**: method

Enables streams for the pipe.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enableStreams() throws
```

#### Discussion

This method changes the operational mode of the pipe to allow streaming endpoint transfers. Call this method before [`copyStream(withStreamID:)`](iousbhostpipe/copystream(withstreamid:).md).

## See Also

- [func copyStream(withStreamID: Int) throws -> IOUSBHostStream](iousbhostpipe/copystream(withstreamid:).md)
  Returns the stream for a stream ID.
- [func disableStreams() throws](iousbhostpipe/disablestreams.md)
  Disables streams for the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/enablestreams())*