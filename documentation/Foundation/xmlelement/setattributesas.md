# setAttributesAs(_:)

**Framework**: Foundation  
**Kind**: method

Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func setAttributesAs(_ attributes: [AnyHashable : Any])
```

#### Discussion

The method uses these names and object values to create [`XMLNode`](xmlnode.md) objects of kind [`XMLNode.Kind.attribute`](xmlnode/kind-swift.enum/attribute.md). Existing attributes are not removed.

## Parameters

- `attributes`: A dictionary of key-value pairs where the attribute name is the key and the object value of the attribute is the dictionary value.

## See Also

- [func addAttribute(XMLNode)](xmlelement/addattribute(_:).md)
  Adds an attribute node to the receiver.
- [func attribute(forName: String) -> XMLNode?](xmlelement/attribute(forname:).md)
  Returns the attribute node of the receiver with the specified name.
- [func attribute(forLocalName: String, uri: String?) -> XMLNode?](xmlelement/attribute(forlocalname:uri:).md)
  Returns the attribute node of the receiver that is identified by a local name and URI.
- [var attributes: [XMLNode]?](xmlelement/attributes.md)
  Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [func removeAttribute(forName: String)](xmlelement/removeattribute(forname:).md)
  Removes an attribute node identified by name.
- [func setAttributesWith([String : String])](xmlelement/setattributeswith(_:).md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/setattributesas(_:))*