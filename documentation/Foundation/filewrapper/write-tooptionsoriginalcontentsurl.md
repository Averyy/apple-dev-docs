# write(to:options:originalContentsURL:)

**Framework**: Foundation  
**Kind**: method

Recursively writes the entire contents of a file wrapper to a given file-system URL.

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
func write(to url: URL, options: FileWrapper.WritingOptions = [], originalContentsURL: URL?) throws
```

#### Discussion

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: URL of the file-system node to which the file wrapper’s contents are written.
- `options`: Option flags for writing to the node located at  . See   for possible values.
- `originalContentsURL`: Specify   for this parameter if there is no earlier version of the contents or if you want to ensure that all the contents are written to files.

## See Also

- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](filewrapper/read(from:options:).md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.
- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [func write(toFile: String, atomically: Bool, updateFilenames: Bool) -> Bool](filewrapper/write(tofile:atomically:updatefilenames:).md)
  Writes a file wrapper’s contents to a given file-system node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/write(to:options:originalcontentsurl:))*