# typeForContents(of:)

**Framework**: AppKit  
**Kind**: method

Returns, for a specified URL, the document type identifier to use when opening the document at that location, if successful.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func typeForContents(of url: URL) throws -> String
```

#### Discussion

The URL is represented by `url`. If not successful, the method returns `nil` after setting `outError` to point to an `NSError` object that encapsulates the reason why the document type could not be determined, or the fact that the document type is unrecognized.

You can override this method to customize type determination for documents being opened.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL to use for locating the type identifier.

## See Also

- [var documentClassNames: [String]](nsdocumentcontroller/documentclassnames.md)
  An array of strings representing the custom document classes supported by this app.
- [var defaultType: String?](nsdocumentcontroller/defaulttype.md)
  Returns the name of the document type that should be used when creating new documents.
- [func documentClass(forType: String) -> AnyClass?](nsdocumentcontroller/documentclass(fortype:).md)
  Returns the `NSDocument` subclass associated with a given document type.
- [func displayName(forType: String) -> String?](nsdocumentcontroller/displayname(fortype:).md)
  Returns the descriptive name for the specified document type, which is used in the File Format pop-up menu of the Save As dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/typeforcontents(of:))*