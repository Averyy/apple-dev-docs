# init(for:withContentsOf:ofType:)

**Framework**: AppKit  
**Kind**: init

Initializes a document with the specified contents, and places the resulting document’s file at the designated location.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
convenience init(for urlOrNil: URL?, withContentsOf contentsURL: URL, ofType typeName: String) throws
```

#### Return Value

The initialized document object, or `nil` if the document could not be created.

#### Discussion

The system calls this method to open a document that has an associated autosave file . You can override this method to handle any document initialization specific to autosave contents.

After reading the contents from the specified autosave file, this method updates the document’s change count using the `NSChangeReadOtherContents` change type.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `urlOrNil`: The location for the document’s file. This value is   for an autosaved document that the user never explicitly saved.
- `contentsURL`: The URL of the file that contains the document’s contents. When loading an autosaved document, this URL contains the location of the autosave file. The contents of this file replace the contents of the file in  .
- `typeName`: The string that identifies the document type.

## See Also

- [init()](nsdocument/init.md)
  Initializes and returns an empty document object.
- [convenience init(contentsOf: URL, ofType: String) throws](nsdocument/init(contentsof:oftype:).md)
  Initializes a document located by a URL of a specified type.
- [convenience init(type: String) throws](nsdocument/init(type:).md)
  Initializes a document of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/init(for:withcontentsof:oftype:))*