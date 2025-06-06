# FileWrapper

**Framework**: Foundation  
**Kind**: class

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

#### Overview

The [`FileWrapper`](filewrapper.md) class provides access to the attributes and contents of file system nodes. A file system node is a file, directory, or symbolic link. Instances of this class are known as file wrappers.

> **Note**:  Starting in macOS 10.7, [`FileWrapper`](filewrapper.md) moved from Application Kit to Foundation. As a result of this the `icon`, and `setIcon:` methods have moved to a new category of [`FileWrapper`](filewrapper.md) that remains in Application Kit.

File wrappers represent a file system node as an object that can be displayed as an image (and possibly edited in place), saved to the file system, or transmitted to another application.

There are three types of file wrappers:

- Regular-file file wrapper: Represents a regular file.
- Directory file wrapper: Represents a directory.
- Symbolic-link file wrapper: Represents a symbolic link.

A file wrapper has these attributes:

- Filename. Name of the file system node the file wrapper represents.
- file-system attributes. See [`FileManager`](filemanager.md) for information on the contents of the `attributes` dictionary.
- Regular-file contents. Applicable only to regular-file file wrappers.
- File wrappers. Applicable only to directory file wrappers.
- Destination node. Applicable only to symbolic-link file wrappers.

## Topics

### Creating File Wrappers
- [init(url: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/init(url:options:).md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [convenience init?(path: String)](filewrapper/init(path:).md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.
- [init(directoryWithFileWrappers: [String : FileWrapper])](filewrapper/init(directorywithfilewrappers:).md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [init(regularFileWithContents: Data)](filewrapper/init(regularfilewithcontents:).md)
  Initializes the receiver as a regular-file file wrapper.
- [convenience init(symbolicLinkWithDestination: String)](filewrapper/init(symboliclinkwithdestination:).md)
  Initializes the receiver as a symbolic-link file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](filewrapper/init(symboliclinkwithdestinationurl:).md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [init?(serializedRepresentation: Data)](filewrapper/init(serializedrepresentation:).md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.
### Querying File Wrappers
- [var isRegularFile: Bool](filewrapper/isregularfile.md)
  This property contains a boolean value that indicates whether the file wrapper object is a regular-file.
- [var isDirectory: Bool](filewrapper/isdirectory.md)
  This property contains a boolean value indicating whether the file wrapper is a directory file wrapper.
- [var isSymbolicLink: Bool](filewrapper/issymboliclink.md)
  A boolean that indicates whether the file wrapper object is a symbolic-link file wrapper.
### Accessing File-Wrapper Information
- [var fileWrappers: [String : FileWrapper]?](filewrapper/filewrappers.md)
  The file wrappers contained by a directory file wrapper.
- [func addFileWrapper(FileWrapper) -> String](filewrapper/addfilewrapper(_:).md)
  Adds a child file wrapper to the receiver, which must be a directory file wrapper.
- [func removeFileWrapper(FileWrapper)](filewrapper/removefilewrapper(_:).md)
  Removes a child file wrapper from the receiver, which must be a directory file wrapper.
- [func addFile(withPath: String) -> String](filewrapper/addfile(withpath:).md)
  Creates a file wrapper from a given file-system node and adds it to the receiver, which must be a directory file wrapper.
- [func addRegularFile(withContents: Data, preferredFilename: String) -> String](filewrapper/addregularfile(withcontents:preferredfilename:).md)
  Creates a regular-file file wrapper with the given contents and adds it to the receiver, which must be a directory file wrapper.
- [func addSymbolicLink(withDestination: String, preferredFilename: String) -> String](filewrapper/addsymboliclink(withdestination:preferredfilename:).md)
  Creates a symbolic-link file wrapper pointing to a given file-system node and adds it to the receiver, which must be a directory file wrapper.
- [func keyForChildFileWrapper(FileWrapper) -> String?](filewrapper/keyforchildfilewrapper(_:).md)
  Returns the dictionary key used by a directory to identify a given file wrapper.
- [func symbolicLinkDestination() -> String](filewrapper/symboliclinkdestination.md)
  Provides the pathname referenced by the file wrapper object, which must be a symbolic-link file wrapper.
- [var symbolicLinkDestinationURL: URL?](filewrapper/symboliclinkdestinationurl.md)
  The URL referenced by the file wrapper object, which must be a symbolic-link file wrapper.
### Updating File Wrappers
- [func needsToBeUpdated(fromPath: String) -> Bool](filewrapper/needstobeupdated(frompath:).md)
  Indicates whether the file wrapper needs to be updated to match a given file-system node.
- [func matchesContents(of: URL) -> Bool](filewrapper/matchescontents(of:).md)
  Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [func update(fromPath: String) -> Bool](filewrapper/update(frompath:).md)
  Updates the file wrapper to match a given file-system node.
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/read(from:options:).md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.
### Serializing
- [var serializedRepresentation: Data?](filewrapper/serializedrepresentation.md)
  The contents of the file wrapper as an opaque data object.
### Accessing Files
- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [var preferredFilename: String?](filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [var regularFileContents: Data?](filewrapper/regularfilecontents.md)
  The contents of the file-system node associated with a regular-file file wrapper.
### Writing Files
- [func write(toFile: String, atomically: Bool, updateFilenames: Bool) -> Bool](filewrapper/write(tofile:atomically:updatefilenames:).md)
  Writes a file wrapper’s contents to a given file-system node.
- [func write(to: URL, options: FileWrapper.WritingOptions, originalContentsURL: URL?) throws](filewrapper/write(to:options:originalcontentsurl:).md)
  Recursively writes the entire contents of a file wrapper to a given file-system URL.
### Working with Icons
- [var icon: NSImage?](filewrapper/icon.md)
  The icon that represents the file wrapper.
### Constants
- [FileWrapper.ReadingOptions](filewrapper/readingoptions.md)
  Reading options that can be set by the [`init(url:options:)`](filewrapper/init(url:options:).md) and [`read(from:options:)`](filewrapper/read(from:options:).md) methods.
- [FileWrapper.WritingOptions](filewrapper/writingoptions.md)
  Writing options that can be set by the [`write(to:options:originalContentsURL:)`](filewrapper/write(to:options:originalcontentsurl:).md) method.
### Initializers
- [init?(coder: NSCoder)](filewrapper/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [class FileHandle](filehandle.md)
  An object-oriented wrapper for a file descriptor.
- [class NSFileSecurity](nsfilesecurity.md)
  A stub class that encapsulates security information about a file.
- [class NSFileVersion](nsfileversion.md)
  A snapshot of a file at a specific point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/filewrapper)*