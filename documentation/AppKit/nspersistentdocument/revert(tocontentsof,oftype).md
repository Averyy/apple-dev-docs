# revert(toContentsOf:ofType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden to clean up the managed object context and controllers during a revert.

**Availability**:
- macOS

## Declaration

```swift
func revert(toContentsOf inAbsoluteURL: URL, ofType inTypeName: String) throws
```

```objc
- (BOOL) revertToContentsOfURL:(NSURL *) inAbsoluteURL ofType:(NSString *) inTypeName error:(NSError **) outError;
```

## Discussion

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inAbsoluteURL`: An URL object that specifies the location of the file to which to revert.
- `inTypeName`: The type of the document at `inAbsoluteURL`.

## See Also

### Document Content Management
- [func read(from: URL, ofType: String) throws](./read%28from,oftype%29.md)
  Sets the contents of the receiver by reading from a file of a given type located by a given URL.
- [func write(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws](./write%28to,oftype,for,originalcontentsurl%29.md)
  Saves changes in the document’s managed object context and saves the document’s persistent store to a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/revert(tocontentsof:oftype:))*