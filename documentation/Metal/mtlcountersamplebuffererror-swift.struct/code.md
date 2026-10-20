# MTLCounterSampleBufferError.Code

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MTLCounterSampleBufferError : NSInteger;
```

## Topics

### Error codes
- [MTLCounterSampleBufferError.Code.outOfMemory](./code/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferError.Code.invalid](./code/invalid.md)
  An error code that indicates when a counter-sample buffer descriptor has at least one invalid property.
- [MTLCounterSampleBufferError.Code.internal](./code/internal.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLCounterSampleBufferError.Code.outOfMemory](./code/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [MTLCounterSampleBufferError.Code.invalid](./code/invalid.md)
  An error code that indicates when a counter-sample buffer descriptor has at least one invalid property.
- [MTLCounterSampleBufferError.Code.internal](./code/internal.md)
  An error code that indicates the Metal framework has an internal problem.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct/code)*