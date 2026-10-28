# typeForContents(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns, for a specified URL, the document type identifier to use when opening the document at that location, if successful.

**Availability**:
- macOS

## Declaration

```swift
func typeForContents(of url: URL) throws -> String
```

```objc
- (NSString *) typeForContentsOfURL:(NSURL *) url error:(NSError **) outError;
```

## Discussion

The URL is represented by `url`. If not successful, the method returns `nil` after setting `outError` to point to an `NSError` object that encapsulates the reason why the document type could not be determined, or the fact that the document type is unrecognized.

You can override this method to customize type determination for documents being opened.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL to use for locating the type identifier.

## See Also

### Managing Document Types
- [var documentClassNames: [String]](./documentclassnames.md)
  An array of strings representing the custom document classes supported by this app.
- [var defaultType: String?](./defaulttype.md)
  Returns the name of the document type that should be used when creating new documents.
- [func documentClass(forType: String) -> AnyClass?](./documentclass%28fortype%29.md)
  Returns the `NSDocument` subclass associated with a given document type.
- [func displayName(forType: String) -> String?](./displayname%28fortype%29.md)
  Returns the descriptive name for the specified document type, which is used in the File Format pop-up menu of the Save As dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/typeforcontents(of:))*