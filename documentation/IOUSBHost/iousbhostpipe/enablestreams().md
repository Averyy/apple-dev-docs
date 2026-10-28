# enableStreams()

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Enables streams for the pipe.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func enableStreams() throws
```

```objc
- (BOOL) enableStreamsWithError:(NSError **) error;
```

## Discussion

This method changes the operational mode of the pipe to allow streaming endpoint transfers. Call this method before [`copyStream(withStreamID:)`](./copystream%28withstreamid%29.md).

## See Also

### Managing Streams
- [func copyStream(withStreamID: Int) throws -> IOUSBHostStream](./copystream%28withstreamid%29.md)
  Returns the stream for a stream ID.
- [func disableStreams() throws](./disablestreams%28%29.md)
  Disables streams for the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/enablestreams())*