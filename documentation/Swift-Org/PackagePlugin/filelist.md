---
url: "https://docs.swift.org/latest/documentation/packageplugin/filelist"
framework: "Swift-Org/PackagePlugin"
---

# FileList

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

Provides information about a list of files.

## Declaration

```swift
struct FileList
```

## Overview

The order is not defined but is guaranteed to be stable. This allows the implementation to be more efficient than a static file list.

## Topics

### Default Implementations
- [BidirectionalCollection Implementations](./filelist/bidirectionalcollection-implementations.md)
- [Collection Implementations](./filelist/collection-implementations.md)
- [RandomAccessCollection Implementations](./filelist/randomaccesscollection-implementations.md)
- [Sequence Implementations](./filelist/sequence-implementations.md)

## Relationships

### Conforms To
- Swift.BidirectionalCollection
- Swift.Collection
- Swift.Copyable
- Swift.Escapable
- Swift.RandomAccessCollection
- Swift.Sequence

## See Also

### Inspecting Package Files
- [struct File](./file.md)
  Information about a single file in a FileList.
- [enum FileType](./filetype.md)
  Information about the type of a file.
- [struct Path](./path.md)
  A simple representation of a path in the file system.
- [struct PathList](./pathlist.md)
  Provides information about a list of paths.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/filelist)*