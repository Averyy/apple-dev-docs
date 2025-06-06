# revert(toContentsOf:ofType:)

**Framework**: Appkit  
**Kind**: method

Overridden to clean up the managed object context and controllers during a revert.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func revert(toContentsOf inAbsoluteURL: URL, ofType inTypeName: String) throws
```

#### Discussion

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inAbsoluteURL`: An URL object that specifies the location of the file to which to revert.
- `inTypeName`: The type of the document at  .

## See Also

- [func read(from: URL, ofType: String) throws](nspersistentdocument/read(from:oftype:).md)
  Sets the contents of the receiver by reading from a file of a given type located by a given URL.
- [func write(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws](nspersistentdocument/write(to:oftype:for:originalcontentsurl:).md)
  Saves changes in the document’s managed object context and saves the document’s persistent store to a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/revert(tocontentsof:oftype:))*