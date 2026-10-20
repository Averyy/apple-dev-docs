# FSError.Code.resourceDamaged

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

The resource is damaged.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case resourceDamaged
```

```c
FSErrorResourceDamaged
```

#### Discussion

This error indicates the resource needs a repair operation, or that a repair operation failed.

> **Note**: The status in this error applies to the resource. A failing repair operation reports a more specific error status.

## See Also

### Identifying errors
- [FSError.Code.invalidDirectoryCookie](./invaliddirectorycookie.md)
  While enumerating a directory, the given cookie didn’t resolve to a valid directory entry.
- [FSError.Code.moduleLoadFailed](./moduleloadfailed.md)
  The module failed to load.
- [FSError.Code.resourceUnrecognized](./resourceunrecognized.md)
  FSKit didn’t recognize the resource, and probing failed to find a match.
- [FSError.Code.resourceUnusable](./resourceunusable.md)
  FSKit recognizes the resource, but the resource isn’t usable.
- [FSError.Code.statusOperationInProgress](./statusoperationinprogress.md)
  An operation is in progress.
- [FSError.Code.statusOperationPaused](./statusoperationpaused.md)
  An operation is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fserror/code/resourcedamaged)*