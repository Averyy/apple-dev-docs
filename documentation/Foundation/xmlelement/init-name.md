# init(name:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSXMLElement` object initialized with the specified name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(name: String)
```

#### Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

#### Discussion

The XML string representation of this object is `<``name``></``name``>`. This method invokes [`init(name:uri:)`](xmlelement/init(name:uri:).md) with the URI parameter set to `nil`.

## Parameters

- `name`: A string specifying the name of the element.

## See Also

- [Tree-Based XML Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html#//apple_ref/doc/uid/TP40001269)
- [convenience init(name: String, stringValue: String?)](xmlelement/init(name:stringvalue:).md)
  Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [init(name: String, uri: String?)](xmlelement/init(name:uri:).md)
  Returns an `NSXMLElement` object initialized with the specified name and URI.
- [init(xmlString: String) throws](xmlelement/init(xmlstring:).md)
  Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](xmlelement/init(kind:options:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/init(name:))*