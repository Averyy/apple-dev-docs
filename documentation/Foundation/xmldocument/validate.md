# validate()

**Framework**: Foundation  
**Kind**: method

Validates the document against the governing schema and returns whether the document conforms to the schema.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func validate() throws
```

#### Discussion

The constants indicating the kind of validation errors are emitted by the underlying parser; see `NSXMLParser.h` for most of these constants. If the schema is defined with a DTD, this method uses the [`XMLDTD`](xmldtd.md) object set for the receiver for validation. If the schema is based on XML Schema, the method uses the URL specified as the value of the `xsi:schemaLocation` attribute of the root element.

You can validate an XML document when it is first processed by specifying the `NSXMLDocumentValidate` option when you initialize an `NSXMLDocument` object with the [`init(contentsOf:options:)`](xmldocument/init(contentsof:options:).md), [`init(data:options:)`](xmldocument/init(data:options:).md), or [`init(xmlString:options:)`](xmldocument/init(xmlstring:options:).md) methods.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/validate())*