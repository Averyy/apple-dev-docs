# init(data:options:)

**Framework**: Foundation  
**Kind**: init

Initializes and returns an `NSXMLDTD` object created from the DTD declarations encapsulated in an [`NSData`](nsdata.md) object

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(data: Data, options mask: XMLNode.Options = []) throws
```

#### Return Value

An initialized `NSXMLDTD` object or `nil` if initialization fails because of parsing errors or other reasons.

#### Discussion

This method is the designated initializer for the `NSXMLDTD` class. You use this method to create a stand-alone DTD which you can thereafter query and use for validation. You can associate the DTD created through this message with a document by setting the [`dtd`](xmldocument/dtd.md) property on an [`XMLDocument`](xmldocument.md) object.

> **Note**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `data`: A data object containing DTD declarations.
- `mask`: A bit mask specifying input options; bit-OR multiple options. The current valid options are   and  ; these constants are described in the “Constants” section of the   reference.

## See Also

- [func validate() throws](xmldocument/validate.md)
  Validates the document against the governing schema and returns whether the document conforms to the schema.
- [convenience init(contentsOf: URL, options: XMLNode.Options) throws](xmldtd/init(contentsof:options:).md)
  Initializes and returns an `NSXMLDTD` object created from the DTD declarations in a URL-referenced source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/init(data:options:))*