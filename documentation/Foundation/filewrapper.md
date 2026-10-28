# FileWrapper

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A representation of a node (a file, directory, or symbolic link) in the file system.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class FileWrapper
```

```objc
@interface NSFileWrapper : NSObject
```

## Overview

The [`FileWrapper`](./filewrapper.md) class provides access to the attributes and contents of file system nodes. A file system node is a file, directory, or symbolic link. Instances of this class are known as file wrappers.

> **Note**:  Starting in macOS 10.7, [`FileWrapper`](./filewrapper.md) moved from Application Kit to Foundation. As a result of this the `icon`, and `setIcon:` methods have moved to a new category of [`FileWrapper`](./filewrapper.md) that remains in Application Kit.

File wrappers represent a file system node as an object that can be displayed as an image (and possibly edited in place), saved to the file system, or transmitted to another application.

There are three types of file wrappers:

- Regular-file file wrapper: Represents a regular file.
- Directory file wrapper: Represents a directory.
- Symbolic-link file wrapper: Represents a symbolic link.

A file wrapper has these attributes:

- Filename. Name of the file system node the file wrapper represents.
- file-system attributes. See [`FileManager`](./filemanager.md) for information on the contents of the `attributes` dictionary.
- Regular-file contents. Applicable only to regular-file file wrappers.
- File wrappers. Applicable only to directory file wrappers.
- Destination node. Applicable only to symbolic-link file wrappers.

## Topics

### Creating File Wrappers
- [init(url: URL, options: FileWrapper.ReadingOptions) throws](./filewrapper/init%28url,options%29-70161.md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [convenience init?(path: String)](./filewrapper/init%28path%29.md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.
- [init(directoryWithFileWrappers: [String : FileWrapper])](./filewrapper/init%28directorywithfilewrappers%29.md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [init(regularFileWithContents: Data)](./filewrapper/init%28regularfilewithcontents%29.md)
  Initializes the receiver as a regular-file file wrapper.
- [convenience init(symbolicLinkWithDestination: String)](./filewrapper/init%28symboliclinkwithdestination%29.md)
  Initializes the receiver as a symbolic-link file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](./filewrapper/init%28symboliclinkwithdestinationurl%29.md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [init?(serializedRepresentation: Data)](./filewrapper/init%28serializedrepresentation%29.md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.
### Querying File Wrappers
- [var isRegularFile: Bool](./filewrapper/isregularfile.md)
  This property contains a boolean value that indicates whether the file wrapper object is a regular-file.
- [var isDirectory: Bool](./filewrapper/isdirectory.md)
  This property contains a boolean value indicating whether the file wrapper is a directory file wrapper.
- [var isSymbolicLink: Bool](./filewrapper/issymboliclink.md)
  A boolean that indicates whether the file wrapper object is a symbolic-link file wrapper.
### Accessing File-Wrapper Information
- [var fileWrappers: [String : FileWrapper]?](./filewrapper/filewrappers.md)
  The file wrappers contained by a directory file wrapper.
- [func addFileWrapper(FileWrapper) -> String](./filewrapper/addfilewrapper%28_%29.md)
  Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [func removeFileWrapper(FileWrapper)](./filewrapper/removefilewrapper%28_%29.md)
  Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [func addFile(withPath: String) -> String](./filewrapper/addfile%28withpath%29.md)
  Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper.
- [func addRegularFile(withContents: Data, preferredFilename: String) -> String](./filewrapper/addregularfile%28withcontents,preferredfilename%29.md)
  Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [func addSymbolicLink(withDestination: String, preferredFilename: String) -> String](./filewrapper/addsymboliclink%28withdestination,preferredfilename%29.md)
  Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper.
- [func keyForChildFileWrapper(FileWrapper) -> String?](./filewrapper/keyforchildfilewrapper%28_%29.md)
  Returns the dictionary key used by a directory to identify a given file wrapper.
- [func symbolicLinkDestination() -> String](./filewrapper/symboliclinkdestination%28%29.md)
  Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper.
- [var symbolicLinkDestinationURL: URL?](./filewrapper/symboliclinkdestinationurl.md)
  The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.
### Updating File Wrappers
- [func needsToBeUpdated(fromPath: String) -> Bool](./filewrapper/needstobeupdated%28frompath%29.md)
  Indicates whether the file wrapper needs to be updated to match a given file-system node.
- [func matchesContents(of: URL) -> Bool](./filewrapper/matchescontents%28of%29.md)
  Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [func update(fromPath: String) -> Bool](./filewrapper/update%28frompath%29.md)
  Updates the file wrapper to match a given file-system node.
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](./filewrapper/read%28from,options%29.md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.
### Serializing
- [var serializedRepresentation: Data?](./filewrapper/serializedrepresentation.md)
  The contents of the file wrapper as an opaque data object.
### Accessing Files
- [var filename: String?](./filewrapper/filename.md)
  The filename of the file wrapper object
- [var preferredFilename: String?](./filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var fileAttributes: [String : Any]](./filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [var regularFileContents: Data?](./filewrapper/regularfilecontents.md)
  The contents of the file-system node associated with a regular-file file wrapper.
### Writing Files
- [func write(toFile: String, atomically: Bool, updateFilenames: Bool) -> Bool](./filewrapper/write%28tofile,atomically,updatefilenames%29.md)
  Writes a file wrapper’s contents to a given file-system node.
- [func write(to: URL, options: FileWrapper.WritingOptions, originalContentsURL: URL?) throws](./filewrapper/write%28to,options,originalcontentsurl%29.md)
  Recursively writes the entire contents of a file wrapper to a given file-system URL.
### Working with Icons
- [var icon: NSImage?](./filewrapper/icon.md)
  The icon that represents the file wrapper.
### Constants
- [FileWrapper.ReadingOptions](./filewrapper/readingoptions.md)
  Reading options that can be set by the [`init(url:options:)`](./filewrapper/init%28url,options%29-70161.md) and [`read(from:options:)`](./filewrapper/read%28from,options%29.md) methods.
- [FileWrapper.WritingOptions](./filewrapper/writingoptions.md)
  Writing options that can be set by the [`write(to:options:originalContentsURL:)`](./filewrapper/write%28to,options,originalcontentsurl%29.md) method.
### Initializers
- [init(URL: URL, options: FileWrapper.ReadingOptions) throws](./filewrapper/init%28url,options%29-6g2yr.md)
- [init?(coder: NSCoder)](./filewrapper/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Managed file access
- [class FileHandle](./filehandle.md)
  An object-oriented wrapper for a file descriptor.
- [class NSFileSecurity](./nsfilesecurity.md)
  A stub class that encapsulates security information about a file.
- [class NSFileVersion](./nsfileversion.md)
  A snapshot of a file at a specific point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper)*