# URL.DirectoryHint.checkFileSystem

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A hint that directs a URL call to consult the file system to determine whether the path references a directory.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case checkFileSystem
```

## See Also

### Hints
- [URL.DirectoryHint.isDirectory](./isdirectory.md)
  A hint that specifies that a given path is a directory.
- [URL.DirectoryHint.notDirectory](./notdirectory.md)
  A hint that specifies that a given path isn’t a directory.
- [URL.DirectoryHint.inferFromPath](./inferfrompath.md)
  A hint that directs a URL call to infer whether a path references a directory based on whether it has a trailing slash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/directoryhint/checkfilesystem)*