# groupingLevel

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number of nested undo groups (or redo groups, if redo is the most recent operation) in the current event loop.

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
var groupingLevel: Int { get }
```

```objc
@property (readonly) NSInteger groupingLevel;
```

#### Discussion

An integer indicating the number of nested groups. If 0 is returned, there is no open undo or redo group.

## See Also

### Related Documentation
- [var levelsOfUndo: Int](./levelsofundo.md)
  The maximum number of top-level undo groups the undo manager holds.
### Creating undo groups
- [func beginUndoGrouping()](./beginundogrouping%28%29.md)
  Marks the beginning of an undo group.
- [func endUndoGrouping()](./endundogrouping%28%29.md)
  Marks the end of an undo group.
- [var groupsByEvent: Bool](./groupsbyevent.md)
  A Boolean value that indicates whether the manager automatically creates undo groups around each pass of the run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/groupinglevel)*