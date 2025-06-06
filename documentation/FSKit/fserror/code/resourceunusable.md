# FSError.Code.resourceUnusable

**Framework**: FSKit  
**Kind**: case

FSKit recognizes the resource, but the resource isn’t usable.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case resourceUnusable
```

#### Discussion

For example, this error occurs when a resource uses a file system’s internal feature flags. If the only modules that support the file system don’t support those feature flags, this code indicates an unusable resource. The error tells the person using the module why the resource isn’t usable.

## See Also

- [FSError.Code.invalidDirectoryCookie](fserror/code/invaliddirectorycookie.md)
  While enumerating a directory, the given cookie didn’t resolve to a valid directory entry.
- [FSError.Code.moduleLoadFailed](fserror/code/moduleloadfailed.md)
  The module failed to load.
- [FSError.Code.resourceDamaged](fserror/code/resourcedamaged.md)
  The resource is damaged.
- [FSError.Code.resourceUnrecognized](fserror/code/resourceunrecognized.md)
  FSKit didn’t recognize the resource, and probing failed to find a match.
- [FSError.Code.statusOperationInProgress](fserror/code/statusoperationinprogress.md)
  An operation is in progress.
- [FSError.Code.statusOperationPaused](fserror/code/statusoperationpaused.md)
  An operation is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fserror/code/resourceunusable)*