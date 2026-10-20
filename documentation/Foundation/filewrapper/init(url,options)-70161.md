# init(url:options:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithURL:(NSURL *) url options:(NSFileWrapperReadingOptions) options error:(NSError **) outError;
```

#### Return Value

File wrapper for the file-system node at `url`. May be a directory, file, or symbolic link, depending on what is located at the URL. Returns [`false`](../../Swift/false.md) (0) if reading is not successful.

#### Discussion

If `url` is a directory, this method recursively creates file wrappers for each node within that directory. Use the [`fileWrappers`](./filewrappers.md) property to get the file wrappers of the nodes contained by the directory.

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: URL of the file-system node the file wrapper is to represent.
- `options`: Option flags for reading the node located at `url`. See [`FileWrapper.ReadingOptions`](./readingoptions.md) for possible values.

## See Also

### Related Documentation
- [var fileWrappers: [String : FileWrapper]?](./filewrappers.md)
  The file wrappers contained by a directory file wrapper.
- [var preferredFilename: String?](./preferredfilename.md)
  The preferred filename for the file wrapper object.
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](./read%28from,options%29.md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.
- [var filename: String?](./filename.md)
  The filename of the file wrapper object
- [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672)
- [var fileAttributes: [String : Any]](./fileattributes.md)
  A dictionary of file attributes.
### Creating File Wrappers
- [convenience init?(path: String)](./init%28path%29.md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.
- [init(directoryWithFileWrappers: [String : FileWrapper])](./init%28directorywithfilewrappers%29.md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [init(regularFileWithContents: Data)](./init%28regularfilewithcontents%29.md)
  Initializes the receiver as a regular-file file wrapper.
- [convenience init(symbolicLinkWithDestination: String)](./init%28symboliclinkwithdestination%29.md)
  Initializes the receiver as a symbolic-link file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](./init%28symboliclinkwithdestinationurl%29.md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.
- [init?(serializedRepresentation: Data)](./init%28serializedrepresentation%29.md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(url:options:)-70161)*