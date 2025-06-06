# FSError.Code.resourceDamaged

**Framework**: Fskit  
**Kind**: case

The resource is damaged.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case resourceDamaged
```

#### Discussion

This error indicates the resource needs a repair operation, or that a repair operation failed.

> **Note**: The status in this error applies to the resource. A failing repair operation reports a more specific error status.

## See Also

- [FSError.Code.invalidDirectoryCookie](fserror/code/invaliddirectorycookie.md)
  While enumerating a directory, the given cookie didn’t resolve to a valid directory entry.
- [FSError.Code.moduleLoadFailed](fserror/code/moduleloadfailed.md)
  The module failed to load.
- [FSError.Code.resourceUnrecognized](fserror/code/resourceunrecognized.md)
  FSKit didn’t recognize the resource, and probing failed to find a match.
- [FSError.Code.resourceUnusable](fserror/code/resourceunusable.md)
  FSKit recognizes the resource, but the resource isn’t usable.
- [FSError.Code.statusOperationInProgress](fserror/code/statusoperationinprogress.md)
  An operation is in progress.
- [FSError.Code.statusOperationPaused](fserror/code/statusoperationpaused.md)
  An operation is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FSKit/fserror/code/resourcedamaged)*