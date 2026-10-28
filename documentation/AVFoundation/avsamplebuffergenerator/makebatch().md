# makeBatch()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a batch object to handle generating multiple sample buffers.

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
func makeBatch() -> AVSampleBufferGeneratorBatch
```

```objc
- (AVSampleBufferGeneratorBatch *) makeBatch;
```

## Return Value

An object to batch generate sample buffers.

## Discussion

Generating sample buffers in batches optimizes performance by allowing the system to asynchronously load sample data and optimize I/O when possible.

## See Also

### Creating a sample buffer
- [func makeSampleBuffer(for: AVSampleBufferRequest) throws -> sending CMSampleBuffer](./makesamplebuffer%28for%29.md)
  Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [func makeSampleBuffer(for: AVSampleBufferRequest, addTo: AVSampleBufferGeneratorBatch) throws -> CMSampleBuffer](./makesamplebuffer%28for,addto%29.md)
  Creates a sample buffer and attempts to defer I/O for its data.
- [func createSampleBuffer(for: AVSampleBufferRequest) -> CMSampleBuffer?](./createsamplebuffer%28for%29.md)
  Creates a new sample buffer reference for the specified buffer request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/makebatch())*