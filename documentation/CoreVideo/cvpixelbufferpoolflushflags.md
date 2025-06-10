# CVPixelBufferPoolFlushFlags

**Framework**: Core Video  
**Kind**: struct

The flags to pass to flush the pool.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct CVPixelBufferPoolFlushFlags
```

## Topics

### Type Properties
- [static var excessBuffers: CVPixelBufferPoolFlushFlags](cvpixelbufferpoolflushflags/excessbuffers.md)
  The value to pass to flush all unused buffers regardless of age.
### Initializers
- [init(rawValue: CVOptionFlags)](cvpixelbufferpoolflushflags/init(rawvalue:).md)
  Creates a pixel buffer pool flush flags set with the options flags that you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class CVPixelBufferPool](cvpixelbufferpool.md)
  A reference to a pixel buffer pool object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags)*