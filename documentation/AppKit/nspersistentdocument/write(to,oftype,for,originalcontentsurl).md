# write(to:ofType:for:originalContentsURL:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Saves changes in the document’s managed object context and saves the document’s persistent store to a given URL.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
func write(to absoluteURL: URL, ofType typeName: String, for saveOperation: NSDocument.SaveOperationType, originalContentsURL absoluteOriginalContentsURL: URL?) throws
```

```objc
- (BOOL) writeToURL:(NSURL *) absoluteURL ofType:(NSString *) typeName forSaveOperation:(NSSaveOperationType) saveOperation originalContentsURL:(NSURL *) absoluteOriginalContentsURL error:(NSError **) error;
```

## Discussion

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `absoluteURL`: An URL that specifies the new location for the document store. It must not be a relative URL.
- `typeName`: The document type.
- `saveOperation`: The save operation type. See the “Constants” section in [`NSDocument`](../nsdocument.md) for possible values.
- `absoluteOriginalContentsURL`: An URL that specifies the location of the original document store.

## See Also

### Related Documentation
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [String : Any]?) throws](./configurepersistentstorecoordinator%28for,oftype,modelconfiguration,storeoptions%29.md)
  Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.
### Document Content Management
- [func read(from: URL, ofType: String) throws](./read%28from,oftype%29.md)
  Sets the contents of the receiver by reading from a file of a given type located by a given URL.
- [func revert(toContentsOf: URL, ofType: String) throws](./revert%28tocontentsof,oftype%29.md)
  Overridden to clean up the managed object context and controllers during a revert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/write(to:oftype:for:originalcontentsurl:))*