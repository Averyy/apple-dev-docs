# init(name:uri:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSXMLElement` object initialized with the specified name and URI.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(name: String, uri URI: String?)
```

#### Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

#### Discussion

You can look up the namespace prefix for this element node based on its URI using [`resolvePrefix(forNamespaceURI:)`](xmlelement/resolveprefix(fornamespaceuri:).md).  This method is the primary initializer for the `NSXMLElement` class.

## Parameters

- `name`: A string that specifies the qualified name of the element.
- `URI`: A string that specifies the namespace URI associated with the element.

## See Also

- [convenience init(name: String)](xmlelement/init(name:).md)
  Returns an `NSXMLElement` object initialized with the specified name.
- [convenience init(name: String, stringValue: String?)](xmlelement/init(name:stringvalue:).md)
  Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [init(xmlString: String) throws](xmlelement/init(xmlstring:).md)
  Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](xmlelement/init(kind:options:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/init(name:uri:))*