# noteFileSystemChanged(_:)

**Framework**: AppKit  
**Kind**: method

Informs the workspace object that the file system changed at the specified path.

**Availability**:
- macOS ?+

## Declaration

```swift
func noteFileSystemChanged(_ path: String)
```

#### Discussion

Avoid calling this method if possible. If you want to track changes to files and directories, use the FSEvents API described in `FSEvents`.

The [`NSWorkspace`](nsworkspace.md) object uses this method to track changes to all the files and directories in which it is interested.

## Parameters

- `path`: The full path that changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/notefilesystemchanged(_:))*