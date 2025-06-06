# FileManager.DirectoryEnumerator

**Framework**: Foundation  
**Kind**: class

An object that enumerates the contents of a directory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class DirectoryEnumerator
```

#### Overview

You obtain a directory enumerator using [`FileManager`](filemanager.md)’s [`enumerator(atPath:)`](filemanager/enumerator(atpath:).md) method. The enumeration provides the pathnames of all files and directories contained within that directory. These pathnames are relative to the directory.

An enumeration is recursive, including the files of all subdirectories, and crosses device boundaries. An enumeration does not resolve symbolic links, or attempt to traverse symbolic links that point to directories.

## Topics

### Getting File and Directory Attributes
- [var directoryAttributes: [FileAttributeKey : Any]?](filemanager/directoryenumerator/directoryattributes.md)
  A dictionary with the attributes of the directory at which enumeration started.
- [var fileAttributes: [FileAttributeKey : Any]?](filemanager/directoryenumerator/fileattributes.md)
  A dictionary with the attributes of the most recently returned file or subdirectory (as referenced by the pathname).
- [var level: Int](filemanager/directoryenumerator/level.md)
  The number of levels deep the current object is in the directory hierarchy being enumerated.
### Skipping Subdirectories
- [func skipDescendents()](filemanager/directoryenumerator/skipdescendents.md)
  Causes the receiver to skip recursion into the most recently obtained subdirectory.
- [func skipDescendants()](filemanager/directoryenumerator/skipdescendants.md)
  Causes the receiver to skip recursion into the most recently obtained subdirectory.
### Instance Properties
- [var isEnumeratingDirectoryPostOrder: Bool](filemanager/directoryenumerator/isenumeratingdirectorypostorder.md)

## Relationships

### Inherits From
- [NSEnumerator](nsenumerator.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSFastEnumeration](nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [func contentsOfDirectory(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions) throws -> [URL]](filemanager/contentsofdirectory(at:includingpropertiesforkeys:options:).md)
  Performs a shallow search of the specified directory and returns URLs for the contained items.
- [func contentsOfDirectory(atPath: String) throws -> [String]](filemanager/contentsofdirectory(atpath:).md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [func enumerator(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions, errorHandler: ((URL, any Error) -> Bool)?) -> FileManager.DirectoryEnumerator?](filemanager/enumerator(at:includingpropertiesforkeys:options:errorhandler:).md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [func enumerator(atPath: String) -> FileManager.DirectoryEnumerator?](filemanager/enumerator(atpath:).md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [func mountedVolumeURLs(includingResourceValuesForKeys: [URLResourceKey]?, options: FileManager.VolumeEnumerationOptions) -> [URL]?](filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:).md)
  Returns an array of URLs that identify the mounted volumes available on the device.
- [FileManager.VolumeEnumerationOptions](filemanager/volumeenumerationoptions.md)
  Options for enumerating mounted volumes with the [`mountedVolumeURLs(includingResourceValuesForKeys:options:)`](filemanager/mountedvolumeurls(includingresourcevaluesforkeys:options:).md) method.
- [func subpathsOfDirectory(atPath: String) throws -> [String]](filemanager/subpathsofdirectory(atpath:).md)
  Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [func subpaths(atPath: String) -> [String]?](filemanager/subpaths(atpath:).md)
  Returns an array of strings identifying the paths for all items in the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator)*