# MTLCounterSampleBufferError

**Framework**: Metal  
**Kind**: struct

The error codes that indicate why a GPU driver can’t create a counter sample buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLCounterSampleBufferError
```

## Topics

### Error Code Values
- [static var outOfMemory: MTLCounterSampleBufferError.Code](mtlcountersamplebuffererror-swift.struct/outofmemory.md)
  An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.
- [static var invalid: MTLCounterSampleBufferError.Code](mtlcountersamplebuffererror-swift.struct/invalid.md)
  An error code that indicates the descriptor for creating a counter sample buffer descriptor has an invalid property.
- [static var `internal`: MTLCounterSampleBufferError.Code](mtlcountersamplebuffererror-swift.struct/internal.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLCounterSampleBufferError.Code](mtlcountersamplebuffererror-swift.struct/code.md)
  The underlying error code type that indicates why a GPU driver can’t create a counter sample buffer.
### Error Domain
- [static var errorDomain: String](mtlcountersamplebuffererror-swift.struct/errordomain.md)
  The current counter sample buffer error domain.
- [let MTLCounterErrorDomain: String](mtlcountererrordomain.md)
  The domain for Metal counter sample buffer errors.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct)*