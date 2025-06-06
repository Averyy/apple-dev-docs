# read(fromFileURL:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: method

Sets the contents of the receiver from the file at the given URL.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
func read(fromFileURL url: URL, options opts: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

#### Discussion

For RTF formatted files, the contents of the file are appended to the previous string instead of replacing the previous string.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The location of the file providing text data.
- `opts`: The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in  .
- `dict`: On return, contains the document attributes. For a list of possible values, see “Document Attributes” in  .

## See Also

- [func read(from: Data, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](nsmutableattributedstring/read(from:options:documentattributes:)-967j7.md)
  Sets the contents of the receiver from the specified data object`.`
- [func read(from: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](nsmutableattributedstring/read(from:options:documentattributes:)-85y1d.md)
  Sets the contents of receiver from the file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(fromfileurl:options:documentattributes:))*