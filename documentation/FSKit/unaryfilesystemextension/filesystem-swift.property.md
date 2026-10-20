# fileSystem

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The instance of your file system type that your app extension provides.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var fileSystem: Self.FileSystem { get }
```

## See Also

### Declaring the implemented file system
- [associatedtype FileSystem : FSUnaryFileSystem, FSUnaryFileSystemOperations](./filesystem-swift.associatedtype.md)
  The type of file system your app extension provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/unaryfilesystemextension/filesystem-swift.property)*