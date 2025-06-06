# levelsOfUndo

**Framework**: Foundation  
**Kind**: property

The maximum number of top-level undo groups the undo manager holds.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var levelsOfUndo: Int { get set }
```

#### Discussion

An integer specifying the number of undo groups. A limit of `0` indicates no limit, so the manager never drops old undo groups.

When ending an undo group results in the number of groups exceeding this limit, the manager drops the oldest groups from the stack. The default is `0`.

If you change the limit to a level below the prior limit, the manager immediately drops old undo groups.

## See Also

- [func enableUndoRegistration()](undomanager/enableundoregistration.md)
  Enables the recording of undo operations.
- [var undoCount: Int](undomanager/undocount.md)
  The number of times you can invoke undo before there are no actions left to undo.
- [var redoCount: Int](undomanager/redocount.md)
  The number of times you can invoke redo before there are no actions left to redo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/levelsofundo)*