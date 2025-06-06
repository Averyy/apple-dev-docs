# read(from:ofType:)

**Framework**: AppKit  
**Kind**: method

Sets the contents of the receiver by reading from a file of a given type located by a given URL.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func read(from absoluteURL: URL, ofType typeName: String) throws
```

#### Discussion

This method sets the URL for the persistent object store associated with the receiver’s managed object context to `absoluteURL`.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `absoluteURL`: An URL that specifies the location from which to read the document.
- `typeName`: The document type at  .

## See Also

- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [String : Any]?) throws](nspersistentdocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md)
  Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.
- [func revert(toContentsOf: URL, ofType: String) throws](nspersistentdocument/revert(tocontentsof:oftype:).md)
  Overridden to clean up the managed object context and controllers during a revert.
- [func write(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws](nspersistentdocument/write(to:oftype:for:originalcontentsurl:).md)
  Saves changes in the document’s managed object context and saves the document’s persistent store to a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/read(from:oftype:))*