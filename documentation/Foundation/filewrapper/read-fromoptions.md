# read(from:options:)

**Framework**: Foundation  
**Kind**: method

Recursively rereads the entire contents of a file wrapper from the specified location on disk.

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
func read(from url: URL, options: FileWrapper.ReadingOptions = []) throws
```

#### Discussion

When reading a directory, children are added and removed as necessary to match the file system.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: URL of the file-system node corresponding to the file wrapper.
- `options`: Option flags for reading the node located at  . See   for possible values.

## See Also

- [var fileWrappers: [String : FileWrapper]?](filewrapper/filewrappers.md)
  The file wrappers contained by a directory file wrapper.
- [init(url: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/init(url:options:).md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [var fileAttributes: [String : Any]](filewrapper/fileattributes.md)
  A dictionary of file attributes.
- [func write(to: URL, options: FileWrapper.WritingOptions, originalContentsURL: URL?) throws](filewrapper/write(to:options:originalcontentsurl:).md)
  Recursively writes the entire contents of a file wrapper to a given file-system URL.
- [func needsToBeUpdated(fromPath: String) -> Bool](filewrapper/needstobeupdated(frompath:).md)
  Indicates whether the file wrapper needs to be updated to match a given file-system node.
- [func matchesContents(of: URL) -> Bool](filewrapper/matchescontents(of:).md)
  Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [func update(fromPath: String) -> Bool](filewrapper/update(frompath:).md)
  Updates the file wrapper to match a given file-system node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/read(from:options:))*