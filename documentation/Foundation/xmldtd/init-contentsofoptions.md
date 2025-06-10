# init(contentsOf:options:)

**Framework**: Foundation  
**Kind**: init

Initializes and returns an `NSXMLDTD` object created from the DTD declarations in a URL-referenced source.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(contentsOf url: URL, options mask: XMLNode.Options = []) throws
```

#### Return Value

An initialized `NSXMLDTD` object or `nil` if initialization fails because of parsing errors or other reasons.

#### Discussion

You use this method to create a stand-alone DTD which you can thereafter query and use for validation. You can associate the DTD created through this message with a document by setting the [`dtd`](xmldocument/dtd.md) property on an [`XMLDocument`](xmldocument.md) object.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: An   object identifying a URL source.
- `mask`: A bit mask specifying input options; bit-OR multiple options. The current valid options are   and  ; these constants are described in the “Constants” section of the   reference.

## See Also

- [func validate() throws](xmldocument/validate.md)
  Validates the document against the governing schema and returns whether the document conforms to the schema.
- [Tree-Based XML Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html#//apple_ref/doc/uid/TP40001269)
- [init(data: Data, options: XMLNode.Options) throws](xmldtd/init(data:options:).md)
  Initializes and returns an `NSXMLDTD` object created from the DTD declarations encapsulated in an [`NSData`](nsdata.md) object


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/init(contentsof:options:))*