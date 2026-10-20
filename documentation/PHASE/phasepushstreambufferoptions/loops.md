# loops

**Framework**: PHASE  
**Kind**: property  
**Role**: Type Property

Indicates a buffer restarts after it finishes processing.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static var loops: PHASEPushStreamBufferOptions { get }
```

```c
PHASEPushStreamBufferLoops
```

## See Also

### Options
- [static var `default`: PHASEPushStreamBufferOptions](./default.md)
  Indicates a buffer processes after existing buffers in the queue.
- [static var interrupts: PHASEPushStreamBufferOptions](./interrupts.md)
  Indicates a buffer begins processing immediately.
- [static var interruptsAtLoop: PHASEPushStreamBufferOptions](./interruptsatloop.md)
  Indicates a buffer begins processing when an existing buffer loops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreambufferoptions/loops)*