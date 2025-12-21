# isCoalescingUndo

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether undo coalescing is in progress.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var isCoalescingUndo: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if undo coalescing is in progress, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func breakUndoCoalescing()](nstextview/breakundocoalescing.md)
  Informs the receiver that it should begin coalescing successive typing operations in a new undo grouping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/iscoalescingundo)*