# makeSampleBuffer(for:)

**Framework**: AVFoundation  
**Kind**: method

Creates a sample buffer, and attempts to load its data asynchronously if requested.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func makeSampleBuffer(for request: AVSampleBufferRequest) throws -> CMSampleBuffer
```

#### Return Value

A sample buffer object.

#### Discussion

If you created the generator with a `nil` timebase, any associated [`AVSampleBufferRequest`](avsamplebufferrequest.md) objects default to using a request mode of [`AVSampleBufferRequest.Mode.immediate`](avsamplebufferrequest/mode-swift.enum/immediate.md).

Call the [`notifyOfDataReady(for:completionHandler:)`](avsamplebuffergenerator/notifyofdataready(for:completionhandler:).md) class method to have the system notify you when sample buffer data is available.

The request may fail based on generator configuration or file format.

## Parameters

- `request`: A sample buffer creation request.

## See Also

- [func makeBatch() -> AVSampleBufferGeneratorBatch](avsamplebuffergenerator/makebatch.md)
  Creates a batch object to handle generating multiple sample buffers.
- [func makeSampleBuffer(for: AVSampleBufferRequest, addTo: AVSampleBufferGeneratorBatch) throws -> CMSampleBuffer](avsamplebuffergenerator/makesamplebuffer(for:addto:).md)
  Creates a sample buffer and attempts to defer I/O for its data.
- [func createSampleBuffer(for: AVSampleBufferRequest) -> CMSampleBuffer?](avsamplebuffergenerator/createsamplebuffer(for:).md)
  Creates a new sample buffer reference for the specified buffer request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/makesamplebuffer(for:))*