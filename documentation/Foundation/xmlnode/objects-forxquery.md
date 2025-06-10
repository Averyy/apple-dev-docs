# objects(forXQuery:)

**Framework**: Foundation  
**Kind**: method

Returns the objects resulting from executing an XQuery query upon the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func objects(forXQuery xquery: String) throws -> [Any]
```

#### Discussion

The receiver acts as the context item for the query (”.”).  If the receiver has been changed after parsing to have multiple adjacent text nodes, you should invoke the `NSXMLElement` method [`normalizeAdjacentTextNodesPreservingCDATA(_:)`](xmlelement/normalizeadjacenttextnodespreservingcdata(_:).md) (with an argument of [`false`](https://developer.apple.com/documentation/swift/false)) to coalesce the text nodes before querying .This convenience method invokes [`objects(forXQuery:constants:)`](xmlnode/objects(forxquery:constants:).md) with `nil` for the `constants` dictionary.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `xquery`: A string that expresses an XQuery query.

## See Also

- [func nodes(forXPath: String) throws -> [XMLNode]](xmlnode/nodes(forxpath:).md)
  Returns the nodes resulting from executing an XPath query upon the receiver.
- [func objects(forXQuery: String, constants: [String : Any]?) throws -> [Any]](xmlnode/objects(forxquery:constants:).md)
  Returns the objects resulting from executing an XQuery query upon the receiver.
- [var xPath: String?](xmlnode/xpath.md)
  Returns the XPath expression identifying the receiver’s location in the document tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/objects(forxquery:))*