# redoCount

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number of times you can invoke redo before there are no actions left to redo.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
var redoCount: Int { get }
```

```objc
@property (readonly) NSUInteger redoCount;
```

## See Also

### Managing undo and redo stack depth
- [var levelsOfUndo: Int](./levelsofundo.md)
  The maximum number of top-level undo groups the undo manager holds.
- [var undoCount: Int](./undocount.md)
  The number of times you can invoke undo before there are no actions left to undo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/redocount)*