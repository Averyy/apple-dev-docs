# MTLCounterSampleBufferError.Code.invalid

**Framework**: Metal  
**Kind**: case

An error code that indicates when a counter-sample buffer descriptor has at least one invalid property.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case invalid
```

#### Discussion

This error applies to the [`MTLDevice`](mtldevice.md) protocol’s [`makeCounterSampleBuffer(descriptor:)`](mtldevice/makecountersamplebuffer(descriptor:).md) method and its [`MTLCounterSampleBufferDescriptor`](mtlcountersamplebufferdescriptor.md) parameter.

## See Also

- [MTLCounterSampleBufferError.Code.outOfMemory](mtlcountersamplebuffererror-swift.struct/code/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferError.Code.internal](mtlcountersamplebuffererror-swift.struct/code/internal.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLCounterSampleBufferError.Code.outOfMemory](mtlcountersamplebuffererror-swift.struct/code/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferError.Code.internal](mtlcountersamplebuffererror-swift.struct/code/internal.md)
  An error code that indicates the Metal framework has an internal problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct/code/invalid)*