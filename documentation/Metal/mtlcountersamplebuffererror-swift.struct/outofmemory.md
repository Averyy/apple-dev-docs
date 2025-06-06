# outOfMemory

**Framework**: Metal  
**Kind**: property

An error code that indicates the GPU device doesn’t have sufficient memory to create a counter sample buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var outOfMemory: MTLCounterSampleBufferError.Code { get }
```

## See Also

- [static var invalid: MTLCounterSampleBufferError.Code](mtlcountersamplebuffererror-swift.struct/invalid.md)
  An error code that indicates the descriptor for creating a counter sample buffer descriptor has an invalid property.
- [static var `internal`: MTLCounterSampleBufferError.Code](mtlcountersamplebuffererror-swift.struct/internal.md)
  An error code that indicates the Metal framework has an internal problem.
- [MTLCounterSampleBufferError.Code](mtlcountersamplebuffererror-swift.struct/code.md)
  The underlying error code type that indicates why a GPU driver can’t create a counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffererror-swift.struct/outofmemory)*