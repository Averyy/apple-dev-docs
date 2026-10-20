# xPath

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the XPath expression identifying the receiver’s location in the document tree.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var xPath: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * XPath;
```

#### Discussion

For example, this method might return a string such as “foo/bar[2]/baz”. The result of this method can be used directly in the [`nodes(forXPath:)`](./nodes%28forxpath%29.md) and [`objects(forXQuery:constants:)`](./objects%28forxquery,constants%29.md) methods.

## See Also

### Executing Queries
- [func nodes(forXPath: String) throws -> [XMLNode]](./nodes%28forxpath%29.md)
  Returns the nodes resulting from executing an XPath query upon the receiver.
- [func objects(forXQuery: String) throws -> [Any]](./objects%28forxquery%29.md)
  Returns the objects resulting from executing an XQuery query upon the receiver.
- [func objects(forXQuery: String, constants: [String : Any]?) throws -> [Any]](./objects%28forxquery,constants%29.md)
  Returns the objects resulting from executing an XQuery query upon the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/xpath)*