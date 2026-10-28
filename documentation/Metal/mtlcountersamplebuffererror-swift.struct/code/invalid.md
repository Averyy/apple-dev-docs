# MTLCounterSampleBufferError.Code.invalid

**Framework**: Metal  
**Kind**: case  
**Role**: Case

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

```c
MTLCounterSampleBufferErrorInvalid
```

## Discussion

This error applies to the [`MTLDevice`](../../mtldevice.md) protocol’s [`makeCounterSampleBuffer(descriptor:)`](../../mtldevice/makecountersamplebuffer%28descriptor%29.md) method and its [`MTLCounterSampleBufferDescriptor`](../../mtlcountersamplebufferdescriptor.md) parameter.

## See Also

### Error codes
- [MTLCounterSampleBufferError.Code.outOfMemory](./outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferError.Code.internal](./internal.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLCounterSampleBufferError.Code.outOfMemory](./outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferError.Code.internal](./internal.md)
  An error code that indicates the Metal framework has an internal problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct/code/invalid)*