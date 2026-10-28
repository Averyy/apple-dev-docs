# FileManager.DirectoryEnumerator

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSDirectoryEnumerator : NSEnumerator
```

## Overview

You obtain a directory enumerator using [`FileManager`](../filemanager.md)’s [`enumerator(atPath:)`](./enumerator%28atpath%29.md) method. The enumeration provides the pathnames of all files and directories contained within that directory. These pathnames are relative to the directory.

An enumeration is recursive, including the files of all subdirectories, and crosses device boundaries. An enumeration does not resolve symbolic links, or attempt to traverse symbolic links that point to directories.

## Topics

### Getting File and Directory Attributes
- [var directoryAttributes: [FileAttributeKey : Any]?](./directoryenumerator/directoryattributes.md)
  A dictionary with the attributes of the directory at which enumeration started.
- [var fileAttributes: [FileAttributeKey : Any]?](./directoryenumerator/fileattributes.md)
  A dictionary with the attributes of the most recently returned file or subdirectory (as referenced by the pathname).
- [var level: Int](./directoryenumerator/level.md)
  The number of levels deep the current object is in the directory hierarchy being enumerated.
### Skipping Subdirectories
- [func skipDescendents()](./directoryenumerator/skipdescendents%28%29.md)
  Causes the receiver to skip recursion into the most recently obtained subdirectory.
- [func skipDescendants()](./directoryenumerator/skipdescendants%28%29.md)
  Causes the receiver to skip recursion into the most recently obtained subdirectory.
### Instance Properties
- [var isEnumeratingDirectoryPostOrder: Bool](./directoryenumerator/isenumeratingdirectorypostorder.md)

## Relationships

### Inherits From
- [NSEnumerator](../nsenumerator.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSFastEnumeration](../nsfastenumeration.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Discovering directory contents
- [func contentsOfDirectory(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions) throws -> [URL]](./contentsofdirectory%28at,includingpropertiesforkeys,options%29.md)
  Performs a shallow search of the specified directory and returns URLs for the contained items.
- [func contentsOfDirectory(atPath: String) throws -> [String]](./contentsofdirectory%28atpath%29.md)
  Performs a shallow search of the specified directory and returns the paths of any contained items.
- [func enumerator(at: URL, includingPropertiesForKeys: [URLResourceKey]?, options: FileManager.DirectoryEnumerationOptions, errorHandler: ((URL, any Error) -> Bool)?) -> FileManager.DirectoryEnumerator?](./enumerator%28at,includingpropertiesforkeys,options,errorhandler%29.md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.
- [func enumerator(atPath: String) -> FileManager.DirectoryEnumerator?](./enumerator%28atpath%29.md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified path.
- [func mountedVolumeURLs(includingResourceValuesForKeys: [URLResourceKey]?, options: FileManager.VolumeEnumerationOptions) -> [URL]?](./mountedvolumeurls%28includingresourcevaluesforkeys,options%29.md)
  Returns an array of URLs that identify the mounted volumes available on the device.
- [FileManager.VolumeEnumerationOptions](./volumeenumerationoptions.md)
  Options for enumerating mounted volumes with the [`mountedVolumeURLs(includingResourceValuesForKeys:options:)`](./mountedvolumeurls%28includingresourcevaluesforkeys,options%29.md) method.
- [func subpathsOfDirectory(atPath: String) throws -> [String]](./subpathsofdirectory%28atpath%29.md)
  Performs a deep enumeration of the specified directory and returns the paths of all of the contained subdirectories.
- [func subpaths(atPath: String) -> [String]?](./subpaths%28atpath%29.md)
  Returns an array of strings identifying the paths for all items in the specified directory.
- [- enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:](../nsfilemanager/enumeratoraturl_includingpropertiesforkeys_options_errorhandler_.md)
  Returns a directory enumerator object that can be used to perform a deep enumeration of the directory at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator)*