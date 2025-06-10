# CVMutablePixelBuffer.Pool.Configuration

**Framework**: Core Video  
**Kind**: struct

Configuration passed to pixel buffer pool on creation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(ageOutDuration: TimeInterval, minimumBufferCount: Int)](cvmutablepixelbuffer/pool/configuration/init(ageoutduration:minimumbuffercount:).md)
  Create new configuration instance
### Instance Properties
- [var ageOutDuration: TimeInterval](cvmutablepixelbuffer/pool/configuration/ageoutduration.md)
  Backing memory of released buffers is kept around for this duration before being freed (default is 1 second). If set to 0, the backing memory of released buffers is freed immediately.
- [var minimumBufferCount: Int](cvmutablepixelbuffer/pool/configuration/minimumbuffercount.md)
  The pool keeps at least this many buffers alive. These buffers do not participate in the age-out mechanism.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/configuration)*