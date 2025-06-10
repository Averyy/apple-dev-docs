# xPath

**Framework**: Foundation  
**Kind**: property

Returns the XPath expression identifying the receiver’s location in the document tree.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var xPath: String? { get }
```

#### Discussion

For example, this method might return a string such as “foo/bar[2]/baz”. The result of this method can be used directly in the [`nodes(forXPath:)`](xmlnode/nodes(forxpath:).md) and [`objects(forXQuery:constants:)`](xmlnode/objects(forxquery:constants:).md) methods.

## See Also

- [func nodes(forXPath: String) throws -> [XMLNode]](xmlnode/nodes(forxpath:).md)
  Returns the nodes resulting from executing an XPath query upon the receiver.
- [func objects(forXQuery: String) throws -> [Any]](xmlnode/objects(forxquery:).md)
  Returns the objects resulting from executing an XQuery query upon the receiver.
- [func objects(forXQuery: String, constants: [String : Any]?) throws -> [Any]](xmlnode/objects(forxquery:constants:).md)
  Returns the objects resulting from executing an XQuery query upon the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/xpath)*