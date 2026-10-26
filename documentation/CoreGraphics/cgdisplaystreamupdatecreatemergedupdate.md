# CGDisplayStreamUpdateCreateMergedUpdate

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

## Declaration

```c
extern CGDisplayStreamUpdateRefCGDisplayStreamUpdateCreateMergedUpdate(CGDisplayStreamUpdateRef firstUpdate, CGDisplayStreamUpdateRef secondUpdate);
```

#### Return Value

The new CGDisplayStreamUpdateRef

#### Discussion

Merge two CGDisplayUpdateRefs into a new one.

In cases where the client wishes to drop certain frame updates, this function may be used to merge two CGDisplayUpdateRefs together.  The core bit of functionality here is generating a new set of refresh/move/dirty rectangle arrays that properly represent the union of the deltas between the two frames.  Note that the ordering of the two refs is important.

## Parameters

- `firstUpdate`: The first update (in a temporal sense)
- `secondUpdate`: The second update (in a temporal sense)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdatecreatemergedupdate)*