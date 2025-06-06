# concurrentDispatch

**Framework**: Metal  
**Kind**: property

A compute command using a grid aligned to threadgroup boundaries.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static var concurrentDispatch: MTLIndirectCommandType { get }
```

## See Also

- [static var draw: MTLIndirectCommandType](mtlindirectcommandtype/draw.md)
  A draw call command.
- [static var drawIndexed: MTLIndirectCommandType](mtlindirectcommandtype/drawindexed.md)
  An indexed draw call command.
- [static var drawPatches: MTLIndirectCommandType](mtlindirectcommandtype/drawpatches.md)
  A draw call command for tessellated patches.
- [static var drawIndexedPatches: MTLIndirectCommandType](mtlindirectcommandtype/drawindexedpatches.md)
  An indexed draw call command for tessellated patches.
- [static var concurrentDispatchThreads: MTLIndirectCommandType](mtlindirectcommandtype/concurrentdispatchthreads.md)
  A compute command using an arbitrarily sized grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandtype/concurrentdispatch)*