# read(from:ofType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the contents of the receiver by reading from a file of a given type located by a given URL.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
func read(from absoluteURL: URL, ofType typeName: String) throws
```

```objc
- (BOOL) readFromURL:(NSURL *) absoluteURL ofType:(NSString *) typeName error:(NSError **) error;
```

#### Discussion

This method sets the URL for the persistent object store associated with the receiver’s managed object context to `absoluteURL`.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `absoluteURL`: An URL that specifies the location from which to read the document.
- `typeName`: The document type at `absoluteURL`.

## See Also

### Related Documentation
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [String : Any]?) throws](./configurepersistentstorecoordinator%28for,oftype,modelconfiguration,storeoptions%29.md)
  Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.
### Document Content Management
- [func revert(toContentsOf: URL, ofType: String) throws](./revert%28tocontentsof,oftype%29.md)
  Overridden to clean up the managed object context and controllers during a revert.
- [func write(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws](./write%28to,oftype,for,originalcontentsurl%29.md)
  Saves changes in the document’s managed object context and saves the document’s persistent store to a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/read(from:oftype:))*