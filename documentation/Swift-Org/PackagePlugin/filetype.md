---
url: "https://docs.swift.org/latest/documentation/packageplugin/filetype"
framework: "Swift-Org/PackagePlugin"
---

# FileType

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

Information about the type of a file.

## Declaration

```swift
enum FileType
```

#### Overview

Future cases will use availability annotations to make sure existing plugins continue to work until they increase their required tools version.

## Topics

### Types of Files
- [FileType.source](./filetype/source.md)
  A source file.
- [FileType.header](./filetype/header.md)
  A header file.
- [FileType.resource](./filetype/resource.md)
  A resource file.
- [FileType.unknown](./filetype/unknown.md)
  A file not covered by any other rule.
### Default Implementations
- [Equatable Implementations](./filetype/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable

## See Also

### Inspecting Package Files
- [struct FileList](./filelist.md)
  Provides information about a list of files.
- [struct File](./file.md)
  Information about a single file in a FileList.
- [struct Path](./path.md)
  A simple representation of a path in the file system.
- [struct PathList](./pathlist.md)
  Provides information about a list of paths.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/filetype)*