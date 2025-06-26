# read(from:options:documentAttributes:)

**Framework**: Foundation  
**Kind**: method

Sets the contents of attributed string using the contents of the specified file.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func read(from url: URL, options opts: [NSAttributedString.DocumentReadingOptionKey : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws
```

#### Discussion

Filter services can be used to convert the contents of the URL into a format recognized by Cocoa.

For RTF formatted files, the contents of the file are appended to the previous string instead of replacing the previous string. Therefore, when using this method with existing content it’s best to clear the content away explicitly.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL of the file to read.
- `opts`: The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in  .
- `dict`: On return, contains the document attributes. For a list of possible values, see “Document Attributes” in  .
- `error`: Upon return, if an error occurs, contains an   object that describes the problem. If you are not interested in possible errors, pass in  .

## See Also

- [func read(from: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsmutableattributedstring/read(from:options:documentattributes:)-5mbcx.md)
  Sets the contents of the attributed string using the specified data object`.`


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-54wth)*