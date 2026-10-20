# skipsSubdirectoryDescendants

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An option to perform a shallow enumeration that doesn’t descend into directories.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var skipsSubdirectoryDescendants: FileManager.DirectoryEnumerationOptions { get }
```

```c
NSDirectoryEnumerationSkipsSubdirectoryDescendants
```

## See Also

### Directory Enumeration Options
- [static var skipsPackageDescendants: FileManager.DirectoryEnumerationOptions](./skipspackagedescendants.md)
  An option to treat packages like files and not descend into their contents.
- [static var skipsHiddenFiles: FileManager.DirectoryEnumerationOptions](./skipshiddenfiles.md)
  An option to skip hidden files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerationoptions/skipssubdirectorydescendants)*