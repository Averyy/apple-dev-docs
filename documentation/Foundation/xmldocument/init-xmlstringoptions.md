# init(xmlString:options:)

**Framework**: Foundation  
**Kind**: init

Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(xmlString string: String, options mask: XMLNode.Options = []) throws
```

#### Return Value

An initialized `NSXMLDocument` object, or `nil` if initialization fails because of parsing errors or other reasons.

#### Discussion

The encoding of the document is set to UTF-8.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `string`: A string object containing XML markup text.
- `mask`: A bit mask for input options. You can specify multiple options by bit-OR’ing them. See Constants for a list of valid input options.

## See Also

- [convenience init(contentsOf: URL, options: XMLNode.Options) throws](xmldocument/init(contentsof:options:).md)
  Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source
- [init(data: Data, options: XMLNode.Options) throws](xmldocument/init(data:options:).md)
  Initializes and returns an `NSXMLDocument` object created from an [`NSData`](nsdata.md) object.
- [init(rootElement: XMLElement?)](xmldocument/init(rootelement:).md)
  Returns an `NSXMLDocument` object initialized with a single child, the root element.
- [class func replacementClass(for: AnyClass) -> AnyClass](xmldocument/replacementclass(for:).md)
  Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/init(xmlstring:options:))*