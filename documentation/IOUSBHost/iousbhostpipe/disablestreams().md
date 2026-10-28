# disableStreams()

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Disables streams for the pipe.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func disableStreams() throws
```

```objc
- (BOOL) disableStreamsWithError:(NSError **) error;
```

## Discussion

This method changes the operational mode of the [`IOUSBHostPipe`](../../kernel/iousbhostpipe.md) to disable streaming endpoint transfers. Before calling this method, set all stream contexts as nonactive on the device through an out-of-band (class-defined) mechanism, in accordance with USB 3.2, 8.12.1.4. This is necessary, as the method synchronously aborts any outstanding calls on existing [`IOUSBHostStream`](../iousbhoststream.md) objects.

## See Also

### Managing Streams
- [func enableStreams() throws](./enablestreams%28%29.md)
  Enables streams for the pipe.
- [func copyStream(withStreamID: Int) throws -> IOUSBHostStream](./copystream%28withstreamid%29.md)
  Returns the stream for a stream ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/disablestreams())*