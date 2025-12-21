# read(from:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: method

Sets the contents of the attributed string using the specified data object`.`

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func read(from data: Data, options opts: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?, error: ()) throws
```

#### Discussion

`opts` can contain one of the values described in the Constants section of NSAttributedString Application Kit Additions Reference (“Option keys for importing documents”).

On return, the `documentAttributes` dictionary (if provided) contains the various keys described in the Constants section of NSAttributedString Application Kit Additions Reference. If unsuccessful, returns NO , after setting `error` to point to an `NSError` object that encapsulates the reason why the attributed string object could not be created.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `data`: The data object providing text data.
- `opts`: Keys specifying the types of documents and other document import options. For a list of possible values, see “Option keys for importing documents” in 
- `dict`: On return, the dictionary (if provided) contains keys representing various document-wide attributes. For a list of possible values, see “Document Attributes” in  .
- `error`: Upon return, if an error occurs, contains an   object that describes the problem. If you are not interested in possible errors, pass in  .

## See Also

- [func read(from: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsmutableattributedstring/read(from:options:documentattributes:)-54wth.md)
  Sets the contents of attributed string using the contents of the specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-5mbcx)*