# MTLCounterSampleBufferError.Code

**Framework**: Metal  
**Kind**: enum

The underlying error code type that indicates why a GPU driver can’t create a counter sample buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error codes
- [MTLCounterSampleBufferError.Code.outOfMemory](mtlcountersamplebuffererror-swift.struct/code/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferError.Code.invalid](mtlcountersamplebuffererror-swift.struct/code/invalid.md)
  An error code that indicates when a counter-sample buffer descriptor has at least one invalid property.
- [MTLCounterSampleBufferError.Code.internal](mtlcountersamplebuffererror-swift.struct/code/internal.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLCounterSampleBufferError.Code.outOfMemory](mtlcountersamplebuffererror-swift.struct/code/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferError.Code.invalid](mtlcountersamplebuffererror-swift.struct/code/invalid.md)
  An error code that indicates when a counter-sample buffer descriptor has at least one invalid property.
- [MTLCounterSampleBufferError.Code.internal](mtlcountersamplebuffererror-swift.struct/code/internal.md)
  An error code that indicates the Metal framework has an internal problem.
### Initializers
- [init?(rawValue: Int)](mtlcountersamplebuffererror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct/code)*