# copyStream(withStreamID:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Returns the stream for a stream ID.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func copyStream(withStreamID streamID: Int) throws -> IOUSBHostStream
```

```objc
- (IOUSBHostStream *) copyStreamWithStreamID:(NSUInteger) streamID error:(NSError **) error;
```

#### Return Value

A pointer to an [`IOUSBHostStream`](../iousbhoststream.md); otherwise, `nil` if the device or the underlying host controller doesn’t support the specified stream ID.

#### Discussion

Call [`enableStreams()`](./enablestreams%28%29.md) before this method.

## Parameters

- `streamID`: A stream ID in the range of 1 to *n*. Retrieve *n* can by calling [`IOUSBGetEndpointMaxStreams(_:_:_:)`](../iousbgetendpointmaxstreams%28_,_,_%29.md) with the [`IOUSBEndpointDescriptor`](../../iokit/iousbendpointdescriptor.md).

## See Also

### Managing Streams
- [func enableStreams() throws](./enablestreams%28%29.md)
  Enables streams for the pipe.
- [func disableStreams() throws](./disablestreams%28%29.md)
  Disables streams for the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/copystream(withstreamid:))*