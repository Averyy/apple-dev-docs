# createSampleBuffer(for:)

**Framework**: AVFoundation  
**Kind**: method

Creates a new sample buffer reference for the specified buffer request.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func createSampleBuffer(for request: AVSampleBufferRequest) -> CMSampleBuffer?
```

#### Return Value

Returns a new `CMSampleBufferRef`.

#### Discussion

It is an error to use an `AVSampleBufferRequest` object with mode set to `AVSampleBufferRequestModeScheduled` when the `AVSampleBufferGenerator` was created with a `NULL` timebase.

## Parameters

- `request`: The sample buffer request.

## See Also

- [func makeSampleBuffer(for: AVSampleBufferRequest) throws -> CMSampleBuffer](avsamplebuffergenerator/makesamplebuffer(for:).md)
  Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [func makeBatch() -> AVSampleBufferGeneratorBatch](avsamplebuffergenerator/makebatch.md)
  Creates a batch object to handle generating multiple sample buffers.
- [func makeSampleBuffer(for: AVSampleBufferRequest, addTo: AVSampleBufferGeneratorBatch) throws -> CMSampleBuffer](avsamplebuffergenerator/makesamplebuffer(for:addto:).md)
  Creates a sample buffer and attempts to defer I/O for its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/createsamplebuffer(for:))*