# CVPixelBufferPoolFlushFlags

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

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

```c
enum CVPixelBufferPoolFlushFlags : CVOptionFlags;
```

## Topics

### Type Properties
- [static var excessBuffers: CVPixelBufferPoolFlushFlags](./cvpixelbufferpoolflushflags/excessbuffers.md)
  The value to pass to flush all unused buffers regardless of age.
### Initializers
- [init(rawValue: CVOptionFlags)](./cvpixelbufferpoolflushflags/init%28rawvalue%29.md)
  Creates a pixel buffer pool flush flags set with the options flags that you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Data types
- [class CVPixelBufferPool](./cvpixelbufferpool.md)
  A reference to a pixel buffer pool object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags)*