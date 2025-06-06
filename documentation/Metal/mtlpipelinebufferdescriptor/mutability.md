# mutability

**Framework**: Metal  
**Kind**: property

A mutability option that determines whether you can update a buffer’s contents before related commands use the buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var mutability: MTLMutability { get set }
```

#### Discussion

The default value is [`MTLMutability.default`](mtlmutability/default.md).

If you don’t explicitly declare mutability, Metal uses the following default behaviors:

- Regular buffers are mutable by default, and Metal treats [`MTLMutability.default`](mtlmutability/default.md) as if it were [`MTLMutability.mutable`](mtlmutability/mutable.md).
- Argument buffers are immutable by default, and Metal treats [`MTLMutability.default`](mtlmutability/default.md) as if it were [`MTLMutability.immutable`](mtlmutability/immutable.md).

## See Also

- [enum MTLMutability](mtlmutability.md)
  The options that determine the mutability of a buffer’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptor/mutability)*