# FSError.Code.moduleLoadFailed

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

The module failed to load.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case moduleLoadFailed
```

```c
FSErrorModuleLoadFailed
```

## See Also

### Identifying errors
- [FSError.Code.invalidDirectoryCookie](./invaliddirectorycookie.md)
  While enumerating a directory, the given cookie didn’t resolve to a valid directory entry.
- [FSError.Code.resourceDamaged](./resourcedamaged.md)
  The resource is damaged.
- [FSError.Code.resourceUnrecognized](./resourceunrecognized.md)
  FSKit didn’t recognize the resource, and probing failed to find a match.
- [FSError.Code.resourceUnusable](./resourceunusable.md)
  FSKit recognizes the resource, but the resource isn’t usable.
- [FSError.Code.statusOperationInProgress](./statusoperationinprogress.md)
  An operation is in progress.
- [FSError.Code.statusOperationPaused](./statusoperationpaused.md)
  An operation is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fserror/code/moduleloadfailed)*