# loops

**Framework**: PHASE  
**Kind**: property

Indicates a buffer restarts after it finishes processing.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var loops: PHASEPushStreamBufferOptions { get }
```

## See Also

- [static var `default`: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/default.md)
  Indicates a buffer processes after existing buffers in the queue.
- [static var interrupts: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/interrupts.md)
  Indicates a buffer begins processing immediately.
- [static var interruptsAtLoop: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/interruptsatloop.md)
  Indicates a buffer begins processing when an existing buffer loops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreambufferoptions/loops)*