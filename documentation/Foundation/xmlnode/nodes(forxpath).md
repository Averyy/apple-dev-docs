# nodes(forXPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the nodes resulting from executing an XPath query upon the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func nodes(forXPath xpath: String) throws -> [XMLNode]
```

```objc
- (NSArray<__kindof NSXMLNode *> *) nodesForXPath:(NSString *) xpath error:(NSError **) error;
```

#### Return Value

An array of `NSXMLNode` objects that match the query, or an empty array if there are no matches.

#### Discussion

The receiver acts as the context item for the query (”.”).  If you have explicitly added adjacent text nodes as children of an element, you should invoke the `NSXMLElement` method [`normalizeAdjacentTextNodesPreservingCDATA(_:)`](../xmlelement/normalizeadjacenttextnodespreservingcdata%28_%29.md) (with an argument of [`false`](../../Swift/false.md)) on the element before applying any XPath queries to it; this method coalesces these text nodes. The same precaution applies if you have processed a document preserving CDATA sections and these sections are adjacent to text nodes.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `xpath`: A string that expresses an XPath query.

## See Also

### Executing Queries
- [func objects(forXQuery: String) throws -> [Any]](./objects%28forxquery%29.md)
  Returns the objects resulting from executing an XQuery query upon the receiver.
- [func objects(forXQuery: String, constants: [String : Any]?) throws -> [Any]](./objects%28forxquery,constants%29.md)
  Returns the objects resulting from executing an XQuery query upon the receiver.
- [var xPath: String?](./xpath.md)
  Returns the XPath expression identifying the receiver’s location in the document tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/nodes(forxpath:))*