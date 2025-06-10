# init(xmlString:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSXMLElement` object created from a specified string containing XML markup.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(xmlString string: String) throws
```

#### Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

#### Discussion

> **Note**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `string`: A string containing XML markup for an element.

## See Also

- [convenience init(name: String)](xmlelement/init(name:).md)
  Returns an `NSXMLElement` object initialized with the specified name.
- [convenience init(name: String, stringValue: String?)](xmlelement/init(name:stringvalue:).md)
  Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [init(name: String, uri: String?)](xmlelement/init(name:uri:).md)
  Returns an `NSXMLElement` object initialized with the specified name and URI.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](xmlelement/init(kind:options:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/init(xmlstring:))*