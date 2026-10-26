---
url: "https://docs.swift.org/latest/documentation/packageplugin/path"
framework: "Swift-Org/PackagePlugin"
---

# Path

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

A simple representation of a path in the file system.

**Availability**:
- Swift 5.6+ - Deprecated in 6.0

## Declaration

```swift
struct Path
```

## Topics

### Initializers
- [init(String)](./path/init%28_%29.md)
  Initializes the path from the contents a string, which should be an absolute path in platform representation.
### Instance Properties
- [var `extension`: String?](./path/extension.md)
  The filename extension, if any (without any leading dot).
- [var lastComponent: String](./path/lastcomponent.md)
  The last path component (including any extension).
- [var stem: String](./path/stem.md)
  The last path component (without any extension).
- [var string: String](./path/string.md)
  A string representation of the path.
### Instance Methods
- [func appending(String...) -> Path](./path/appending%28_%29-3f7dc.md)
  The result of appending one or more path components.
- [func appending([String]) -> Path](./path/appending%28_%29-bdm3.md)
  The result of appending one or more path components.
- [func appending(subpath: String) -> Path](./path/appending%28subpath%29.md)
  The result of appending a subpath, which should be a relative path in platform representation.
- [func removingLastComponent() -> Path](./path/removinglastcomponent%28%29.md)
  The path except for the last path component.
### Default Implementations
- [CustomStringConvertible Implementations](./path/customstringconvertible-implementations.md)
- [Decodable Implementations](./path/decodable-implementations.md)
- [Encodable Implementations](./path/encodable-implementations.md)
- [Equatable Implementations](./path/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Escapable
- Swift.Hashable

## See Also

### Inspecting Package Files
- [struct FileList](./filelist.md)
  Provides information about a list of files.
- [struct File](./file.md)
  Information about a single file in a FileList.
- [enum FileType](./filetype.md)
  Information about the type of a file.
- [struct PathList](./pathlist.md)
  Provides information about a list of paths.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/path)*