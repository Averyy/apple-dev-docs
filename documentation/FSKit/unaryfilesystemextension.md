# UnaryFileSystemExtension

**Framework**: FSKit  
**Kind**: protocol

A protocol for implementing a minimal file system as an app extension.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol UnaryFileSystemExtension : AppExtension
```

#### Overview

Your app needs to do the following to implement a FSKit-compatible minimal file system:

1. Create a subclass of [`FSUnaryFileSystem`](fsunaryfilesystem.md), which also conforms to [`FSUnaryFileSystemOperations`](fsunaryfilesystemoperations.md).
2. Implement a `@main` struct that conforms to the `UnaryFileSystemExtension` protocol. Your implementation of this protocol returns the type of class from step 1 as its [`FileSystem`](unaryfilesystemextension/filesystem-swift.associatedtype.md) associated type, and returns an instance of it as the [`fileSystem`](unaryfilesystemextension/filesystem-swift.property.md) property.

## Topics

### Associated Types
- [associatedtype FileSystem : FSUnaryFileSystem, FSUnaryFileSystemOperations](unaryfilesystemextension/filesystem-swift.associatedtype.md)
  The type of file system your app extension provides.
### Instance Properties
- [var fileSystem: Self.FileSystem](unaryfilesystemextension/filesystem-swift.property.md)
  The instance of your file system type that your app extension provides.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/unaryfilesystemextension)*