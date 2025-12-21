# CMBlockBuffer.Slice

**Framework**: Core Media  
**Kind**: struct

A slice of a `CMBlockBuffer` instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Slice
```

#### Overview

> ❗ **Important**: Long-term storage of `CMBlockBuffer.Slice` instances is discouraged. A slice holds a reference to the entire storage of a larger block buffer, not just to the portion it presents, even after the original buffer’s lifetime ends. Long-term storage of a slice may therefore prolong the lifetime of bytes that are no longer otherwise accessible, which can appear to be memory and object leakage.

## Relationships

### Conforms To
- [CMBlockBufferProtocol](cmblockbufferprotocol.md)
- [Copyable](../Swift/Copyable.md)

## See Also

- [CMBlockBuffer.Error](cmblockbuffer/error.md)
  A structure that defines block buffer errors.
- [CMBlockBuffer.Flags](cmblockbuffer/flags.md)
  A structure that defines feature and control flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffer/slice)*