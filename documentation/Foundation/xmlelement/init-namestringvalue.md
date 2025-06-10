# init(name:stringValue:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(name: String, stringValue string: String?)
```

#### Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

#### Discussion

The string representation of this object is `<``name``>``string``</``name``>`.

## Parameters

- `name`: A string specifying the name of the element.
- `string`: The string value of the receiver’s text node.

## See Also

- [convenience init(name: String)](xmlelement/init(name:).md)
  Returns an `NSXMLElement` object initialized with the specified name.
- [init(name: String, uri: String?)](xmlelement/init(name:uri:).md)
  Returns an `NSXMLElement` object initialized with the specified name and URI.
- [init(xmlString: String) throws](xmlelement/init(xmlstring:).md)
  Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](xmlelement/init(kind:options:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/init(name:stringvalue:))*