# FSError.Code.statusOperationPaused

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

An operation is paused.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case statusOperationPaused
```

```c
FSErrorStatusOperationPaused
```

## See Also

### Identifying errors
- [FSError.Code.invalidDirectoryCookie](./invaliddirectorycookie.md)
  While enumerating a directory, the given cookie didn’t resolve to a valid directory entry.
- [FSError.Code.moduleLoadFailed](./moduleloadfailed.md)
  The module failed to load.
- [FSError.Code.resourceDamaged](./resourcedamaged.md)
  The resource is damaged.
- [FSError.Code.resourceUnrecognized](./resourceunrecognized.md)
  FSKit didn’t recognize the resource, and probing failed to find a match.
- [FSError.Code.resourceUnusable](./resourceunusable.md)
  FSKit recognizes the resource, but the resource isn’t usable.
- [FSError.Code.statusOperationInProgress](./statusoperationinprogress.md)
  An operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fserror/code/statusoperationpaused)*