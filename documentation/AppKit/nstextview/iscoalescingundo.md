# isCoalescingUndo

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether undo coalescing is in progress.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isCoalescingUndo: Bool { get }
```

```objc
@property (readonly, getter=isCoalescingUndo) BOOL coalescingUndo;
```

## Discussion

[`true`](../../Swift/true.md) if undo coalescing is in progress, otherwise [`false`](../../Swift/false.md).

## See Also

### Supporting undo
- [func breakUndoCoalescing()](./breakundocoalescing%28%29.md)
  Informs the receiver that it should begin coalescing successive typing operations in a new undo grouping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/iscoalescingundo)*