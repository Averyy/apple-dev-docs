# init(data:options:)

**Framework**: Foundation  
**Kind**: init

Initializes and returns an `NSXMLDocument` object created from an [`NSData`](nsdata.md) object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(data: Data, options mask: XMLNode.Options = []) throws
```

#### Return Value

An initialized `NSXMLDocument` object, or  `nil` if initialization fails because of parsing errors or other reasons.

#### Discussion

This method is the designated initializer for the `NSXMLDocument` class.

If you specify `NSXMLDocumentTidyXML` as one of the options, NSXMLDocument performs several clean-up operations on the document XML (such as removing leading tabs). It does respect the `xml:space="preserve"` attribute when it attempts to tidy the XML.

> **Note**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `data`: A data object with XML content.
- `mask`: A bit mask for input options. You can specify multiple options by bit-OR’ing them. See Constants for a list of valid input options.

## See Also

- [convenience init(contentsOf: URL, options: XMLNode.Options) throws](xmldocument/init(contentsof:options:).md)
  Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source
- [init(rootElement: XMLElement?)](xmldocument/init(rootelement:).md)
  Returns an `NSXMLDocument` object initialized with a single child, the root element.
- [convenience init(xmlString: String, options: XMLNode.Options) throws](xmldocument/init(xmlstring:options:).md)
  Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.
- [class func replacementClass(for: AnyClass) -> AnyClass](xmldocument/replacementclass(for:).md)
  Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/init(data:options:))*