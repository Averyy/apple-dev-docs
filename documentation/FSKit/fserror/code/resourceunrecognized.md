# FSError.Code.resourceUnrecognized

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

FSKit didn’t recognize the resource, and probing failed to find a match.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case resourceUnrecognized
```

```c
FSErrorResourceUnrecognized
```

## See Also

### Identifying errors
- [FSError.Code.invalidDirectoryCookie](./invaliddirectorycookie.md)
  While enumerating a directory, the given cookie didn’t resolve to a valid directory entry.
- [FSError.Code.moduleLoadFailed](./moduleloadfailed.md)
  The module failed to load.
- [FSError.Code.resourceDamaged](./resourcedamaged.md)
  The resource is damaged.
- [FSError.Code.resourceUnusable](./resourceunusable.md)
  FSKit recognizes the resource, but the resource isn’t usable.
- [FSError.Code.statusOperationInProgress](./statusoperationinprogress.md)
  An operation is in progress.
- [FSError.Code.statusOperationPaused](./statusoperationpaused.md)
  An operation is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fserror/code/resourceunrecognized)*