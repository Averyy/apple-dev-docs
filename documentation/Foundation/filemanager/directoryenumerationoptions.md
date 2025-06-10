# FileManager.DirectoryEnumerationOptions

**Framework**: Foundation  
**Kind**: struct

Options for enumerating the contents of directories.

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
struct DirectoryEnumerationOptions
```

#### Overview

These options are used with the [`contentsOfDirectory(at:includingPropertiesForKeys:options:)`](filemanager/contentsofdirectory(at:includingpropertiesforkeys:options:).md) method.

## Topics

### Creating a Directory Enumeration Options Value
- [init(rawValue: UInt)](filemanager/directoryenumerationoptions/init(rawvalue:).md)
  Creates a directory enumeration options value.
### Directory Enumeration Options
- [static var skipsSubdirectoryDescendants: FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions/skipssubdirectorydescendants.md)
  An option to perform a shallow enumeration that doesn’t descend into directories.
- [static var skipsPackageDescendants: FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions/skipspackagedescendants.md)
  An option to treat packages like files and not descend into their contents.
- [static var skipsHiddenFiles: FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions/skipshiddenfiles.md)
  An option to skip hidden files.
### Type Properties
- [static var includesDirectoriesPostOrder: FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions/includesdirectoriespostorder.md)
- [static var producesRelativePathURLs: FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions/producesrelativepathurls.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [FileManager.SearchPathDirectory](filemanager/searchpathdirectory.md)
  The location of significant directories.
- [FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask.md)
  Domain constants specifying base locations to use when you search for significant directories.
- [struct FileAttributeKey](fileattributekey.md)
  Keys in dictionaries used to get and set file attributes.
- [struct FileAttributeType](fileattributetype.md)
  Values representing a file’s type attribute.
- [struct FileProtectionType](fileprotectiontype.md)
  Protection level values that can be associated with a file attribute key.
- [struct URLFileProtection](urlfileprotection.md)
  Protection-level values for a URL resource key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerationoptions)*