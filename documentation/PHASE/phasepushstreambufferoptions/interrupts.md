# interrupts

**Framework**: PHASE  
**Kind**: property

Indicates a buffer begins processing immediately.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var interrupts: PHASEPushStreamBufferOptions { get }
```

## See Also

- [static var `default`: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/default.md)
  Indicates a buffer processes after existing buffers in the queue.
- [static var interruptsAtLoop: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/interruptsatloop.md)
  Indicates a buffer begins processing when an existing buffer loops.
- [static var loops: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/loops.md)
  Indicates a buffer restarts after it finishes processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreambufferoptions/interrupts)*