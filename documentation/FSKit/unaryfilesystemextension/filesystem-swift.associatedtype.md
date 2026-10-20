# FileSystem

**Framework**: FSKit  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of file system your app extension provides.

**Availability**:
- macOS 15.4+

## Declaration

```swift
associatedtype FileSystem : FSUnaryFileSystem, FSUnaryFileSystemOperations
```

## See Also

### Declaring the implemented file system
- [var fileSystem: Self.FileSystem](./filesystem-swift.property.md)
  The instance of your file system type that your app extension provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/unaryfilesystemextension/filesystem-swift.associatedtype)*