# write(to:options:originalContentsURL:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) writeToURL:(NSURL *) url options:(NSFileWrapperWritingOptions) options originalContentsURL:(NSURL *) originalContentsURL error:(NSError **) outError;
```

#### Discussion

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: URL of the file-system node to which the file wrapper’s contents are written.
- `options`: Option flags for writing to the node located at `url`. See [`FileWrapper.WritingOptions`](./writingoptions.md) for possible values.
- `originalContentsURL`: The location of a previous revision of the contents being written. The default implementation of this method attempts to avoid unnecessary I/O by writing hard links to regular files instead of actually writing out their contents when the contents have not changed.  The child file wrappers must return accurate values when its [`filename`](./filename.md) property is accessed for this to work. Use the `NSFileWrapperWritingWithNameUpdating` writing option to increase the likelihood of that.

  Specify `nil` for this parameter if there is no earlier version of the contents or if you want to ensure that all the contents are written to files.

## See Also

### Related Documentation
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](./read%28from,options%29.md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.
- [var filename: String?](./filename.md)
  The filename of the file wrapper object
### Writing Files
- [func write(toFile: String, atomically: Bool, updateFilenames: Bool) -> Bool](./write%28tofile,atomically,updatefilenames%29.md)
  Writes a file wrapper’s contents to a given file-system node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/write(to:options:originalcontentsurl:))*