# init(url:options:)

**Framework**: Foundation  
**Kind**: init

Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.

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
init(url: URL, options: FileWrapper.ReadingOptions = []) throws
```

#### Return Value

File wrapper for the file-system node at `url`. May be a directory, file, or symbolic link, depending on what is located at the URL. Returns [`false`](https://developer.apple.com/documentation/Swift/false) (0) if reading is not successful.

#### Discussion

If `url` is a directory, this method recursively creates file wrappers for each node within that directory. Use the [`fileWrappers`](filewrapper/filewrappers.md) property to get the file wrappers of the nodes contained by the directory.

> **Note**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: URL of the file-system node the file wrapper is to represent.
- `options`: Option flags for reading the node located at  . See   for possible values.

## See Also

- [var fileWrappers: [String : FileWrapper]?](filewrapper/filewrappers.md)
  The file wrappers contained by a directory file wrapper.
- [var preferredFilename: String?](filewrapper/preferredfilename.md)
  The preferred filename for the file wrapper object.
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/read(from:options:).md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.
- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [File System Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672)
- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(url:options:))*