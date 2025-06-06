# MTLMutability

**Framework**: Metal  
**Kind**: enum

The options that determine the mutability of a buffer’s contents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLMutability
```

## Topics

### Enumeration Cases
- [MTLMutability.default](mtlmutability/default.md)
  The default behavior, based on the buffer’s type.
- [MTLMutability.mutable](mtlmutability/mutable.md)
  An option that states that you can modify the buffer’s contents.
- [MTLMutability.immutable](mtlmutability/immutable.md)
  An option that states that you can’t modify the buffer’s contents.
### Initializers
- [init?(rawValue: UInt)](mtlmutability/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var mutability: MTLMutability](mtlpipelinebufferdescriptor/mutability.md)
  A mutability option that determines whether you can update a buffer’s contents before related commands use the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmutability)*