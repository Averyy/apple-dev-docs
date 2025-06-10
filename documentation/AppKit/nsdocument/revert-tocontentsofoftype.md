# revert(toContentsOf:ofType:)

**Framework**: AppKit  
**Kind**: method

Discards all unsaved document modifications and replaces the document’s contents by reading a file or file package located by a URL of a specified type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func revert(toContentsOf url: URL, ofType typeName: String) throws
```

#### Discussion

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The location from which the document contents are read.
- `typeName`: The string that identifies the document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/revert(tocontentsof:oftype:))*