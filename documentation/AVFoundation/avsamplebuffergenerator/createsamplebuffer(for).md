# createSampleBuffer(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a new sample buffer reference for the specified buffer request.

**Availability**:
- macOS 10.10+ - Deprecated in 13.0

> **Deprecated**: Use -createSampleBufferForRequest: error:, passing NULL for the error if not required

## Declaration

```swift
func createSampleBuffer(for request: AVSampleBufferRequest) -> CMSampleBuffer?
```

```objc
- (CMSampleBufferRef) createSampleBufferForRequest:(AVSampleBufferRequest *) request;
```

#### Return Value

Returns a new `CMSampleBufferRef`.

#### Discussion

It is an error to use an `AVSampleBufferRequest` object with mode set to `AVSampleBufferRequestModeScheduled` when the `AVSampleBufferGenerator` was created with a `NULL` timebase.

## Parameters

- `request`: The sample buffer request.

## See Also

### Creating a sample buffer
- [func makeSampleBuffer(for: AVSampleBufferRequest) throws -> sending CMSampleBuffer](./makesamplebuffer%28for%29.md)
  Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [func makeBatch() -> AVSampleBufferGeneratorBatch](./makebatch%28%29.md)
  Creates a batch object to handle generating multiple sample buffers.
- [func makeSampleBuffer(for: AVSampleBufferRequest, addTo: AVSampleBufferGeneratorBatch) throws -> CMSampleBuffer](./makesamplebuffer%28for,addto%29.md)
  Creates a sample buffer and attempts to defer I/O for its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/createsamplebuffer(for:))*