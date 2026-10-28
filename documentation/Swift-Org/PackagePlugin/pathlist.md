---
url: "https://docs.swift.org/latest/documentation/packageplugin/pathlist"
framework: "Swift-Org/PackagePlugin"
---

# PathList

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

Provides information about a list of paths.

**Availability**:
- Swift 5.6+ - Deprecated in 6.0

## Declaration

```swift
struct PathList
```

## Overview

The order is not defined but is guaranteed to be stable. This allows the implementation to be more efficient than a static path list.

## Topics

### Default Implementations
- [Sequence Implementations](./pathlist/sequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sequence

## See Also

### Inspecting Package Files
- [struct FileList](./filelist.md)
  Provides information about a list of files.
- [struct File](./file.md)
  Information about a single file in a FileList.
- [enum FileType](./filetype.md)
  Information about the type of a file.
- [struct Path](./path.md)
  A simple representation of a path in the file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/pathlist)*