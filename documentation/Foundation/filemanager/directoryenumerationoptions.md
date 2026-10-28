# FileManager.DirectoryEnumerationOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSDirectoryEnumerationOptions : NSUInteger;
```

## Overview

These options are used with the [`contentsOfDirectory(at:includingPropertiesForKeys:options:)`](./contentsofdirectory%28at,includingpropertiesforkeys,options%29.md) method.

## Topics

### Creating a Directory Enumeration Options Value
- [init(rawValue: UInt)](./directoryenumerationoptions/init%28rawvalue%29.md)
  Creates a directory enumeration options value.
### Directory Enumeration Options
- [static var skipsSubdirectoryDescendants: FileManager.DirectoryEnumerationOptions](./directoryenumerationoptions/skipssubdirectorydescendants.md)
  An option to perform a shallow enumeration that doesn’t descend into directories.
- [static var skipsPackageDescendants: FileManager.DirectoryEnumerationOptions](./directoryenumerationoptions/skipspackagedescendants.md)
  An option to treat packages like files and not descend into their contents.
- [static var skipsHiddenFiles: FileManager.DirectoryEnumerationOptions](./directoryenumerationoptions/skipshiddenfiles.md)
  An option to skip hidden files.
### Type Properties
- [static var includesDirectoriesPostOrder: FileManager.DirectoryEnumerationOptions](./directoryenumerationoptions/includesdirectoriespostorder.md)
  An option to skip hidden files.
- [static var producesRelativePathURLs: FileManager.DirectoryEnumerationOptions](./directoryenumerationoptions/producesrelativepathurls.md)
  An option to skip hidden files.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Supporting Types
- [FileManager.SearchPathDirectory](./searchpathdirectory.md)
  The location of significant directories.
- [FileManager.SearchPathDomainMask](./searchpathdomainmask.md)
  Domain constants specifying base locations to use when you search for significant directories.
- [struct FileAttributeKey](../fileattributekey.md)
  Keys in dictionaries used to get and set file attributes.
- [struct FileAttributeType](../fileattributetype.md)
  Values representing a file’s type attribute.
- [struct FileProtectionType](../fileprotectiontype.md)
  Protection level values that can be associated with a file attribute key.
- [struct URLFileProtection](../urlfileprotection.md)
  Protection-level values for a URL resource key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerationoptions)*