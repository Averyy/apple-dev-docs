# drawPatches

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

A draw call command for tessellated patches.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
static var drawPatches: MTLIndirectCommandType { get }
```

```c
MTLIndirectCommandTypeDrawPatches
```

## See Also

### Specifying command types
- [static var draw: MTLIndirectCommandType](./draw.md)
  A draw call command.
- [static var drawIndexed: MTLIndirectCommandType](./drawindexed.md)
  An indexed draw call command.
- [static var drawIndexedPatches: MTLIndirectCommandType](./drawindexedpatches.md)
  An indexed draw call command for tessellated patches.
- [static var concurrentDispatch: MTLIndirectCommandType](./concurrentdispatch.md)
  A compute command using a grid aligned to threadgroup boundaries.
- [static var concurrentDispatchThreads: MTLIndirectCommandType](./concurrentdispatchthreads.md)
  A compute command using an arbitrarily sized grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandtype/drawpatches)*