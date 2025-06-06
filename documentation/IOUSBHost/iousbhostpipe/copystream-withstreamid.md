# copyStream(withStreamID:)

**Framework**: IOUSBHost  
**Kind**: method

Returns the stream for a stream ID.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func copyStream(withStreamID streamID: Int) throws -> IOUSBHostStream
```

#### Return Value

A pointer to an [`IOUSBHostStream`](iousbhoststream.md); otherwise, `nil` if the device or the underlying host controller doesn’t support the specified stream ID.

#### Discussion

Call [`enableStreams()`](iousbhostpipe/enablestreams().md) before this method.

## Parameters

- `streamID`: A stream ID in the range of 1 to  . Retrieve   can by calling   with the  .

## See Also

- [func enableStreams() throws](iousbhostpipe/enablestreams.md)
  Enables streams for the pipe.
- [func disableStreams() throws](iousbhostpipe/disablestreams.md)
  Disables streams for the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/copystream(withstreamid:))*