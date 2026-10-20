# interrupts

**Framework**: PHASE  
**Kind**: property  
**Role**: Type Property

Indicates a buffer begins processing immediately.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static var interrupts: PHASEPushStreamBufferOptions { get }
```

```c
PHASEPushStreamBufferInterrupts
```

## See Also

### Options
- [static var `default`: PHASEPushStreamBufferOptions](./default.md)
  Indicates a buffer processes after existing buffers in the queue.
- [static var interruptsAtLoop: PHASEPushStreamBufferOptions](./interruptsatloop.md)
  Indicates a buffer begins processing when an existing buffer loops.
- [static var loops: PHASEPushStreamBufferOptions](./loops.md)
  Indicates a buffer restarts after it finishes processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreambufferoptions/interrupts)*