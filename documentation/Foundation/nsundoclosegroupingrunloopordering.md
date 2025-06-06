# NSUndoCloseGroupingRunLoopOrdering

**Framework**: Foundation  
**Kind**: var

A priority to use when using a run loop to close an undo group.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSUndoCloseGroupingRunLoopOrdering: Int
```

#### Discussion

Use this value as the `order` parameter if you call [`perform(_:target:argument:order:modes:)`](runloop/perform(_:target:argument:order:modes:).md) to have a [`RunLoop`](runloop.md) perform a selector that closes an undo group.

## See Also

- [var runLoopModes: [RunLoop.Mode]](undomanager/runloopmodes.md)
  The modes governing the types of input to handle during a cycle of the run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsundoclosegroupingrunloopordering)*