# makeSampleBuffer(for:addTo:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a sample buffer and attempts to defer I/O for its data.

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
func makeSampleBuffer(for request: AVSampleBufferRequest, addTo batch: AVSampleBufferGeneratorBatch) throws -> CMSampleBuffer
```

```objc
- (CMSampleBufferRef) createSampleBufferForRequest:(AVSampleBufferRequest *) request addingToBatch:(AVSampleBufferGeneratorBatch *) batch error:(NSError **) outError;
```

#### Return Value

A sample buffer.

#### Discussion

Call the [`makeDataReady(completionHandler:)`](../avsamplebuffergeneratorbatch/makedataready%28completionhandler%29.md) on [`AVSampleBufferGeneratorBatch`](../avsamplebuffergeneratorbatch.md) once to commence I/O and load sample data for all [`CMSampleBuffer`](../../CoreMedia/cmsamplebuffer.md) objects in a batch. After loading commences, any subsequent calls to [`makeSampleBuffer(for:addTo:)`](./makesamplebuffer%28for,addto%29.md) throw an exception.

The generator may defer I/O to fetch sample data depending on the source of the sample data and the generator’s timebase

The request may fail based on generator configuration or file format.

## Parameters

- `request`: A sample buffer creation request.
- `batch`: A batch object to contain the output sample buffer. You must create this object by calling [`makeBatch()`](./makebatch%28%29.md) on the same instance of [`AVSampleBufferGenerator`](../avsamplebuffergenerator.md) or an error occurs.

## See Also

### Creating a sample buffer
- [func makeSampleBuffer(for: AVSampleBufferRequest) throws -> sending CMSampleBuffer](./makesamplebuffer%28for%29.md)
  Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [func makeBatch() -> AVSampleBufferGeneratorBatch](./makebatch%28%29.md)
  Creates a batch object to handle generating multiple sample buffers.
- [func createSampleBuffer(for: AVSampleBufferRequest) -> CMSampleBuffer?](./createsamplebuffer%28for%29.md)
  Creates a new sample buffer reference for the specified buffer request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/makesamplebuffer(for:addto:))*