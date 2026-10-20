# CVMutablePixelBuffer.Pool.Configuration

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

Configuration passed to pixel buffer pool on creation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(ageOutDuration: TimeInterval, minimumBufferCount: Int)](./configuration/init%28ageoutduration,minimumbuffercount%29.md)
  Create new configuration instance
### Instance Properties
- [var ageOutDuration: TimeInterval](./configuration/ageoutduration.md)
  Backing memory of released buffers is kept around for this duration before being freed (default is 1 second). If set to 0, the backing memory of released buffers is freed immediately.
- [var minimumBufferCount: Int](./configuration/minimumbuffercount.md)
  The pool keeps at least this many buffers alive. These buffers do not participate in the age-out mechanism.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/configuration)*