# attributes

**Framework**: Foundation  
**Kind**: property

Sets all attributes of the receiver at once, replacing any existing attribute nodes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var attributes: [XMLNode]? { get set }
```

#### Discussion

To set attributes in an element node using an [`NSDictionary`](nsdictionary.md) object as the input parameter, see [`setAttributesWith(_:)`](xmlelement/setattributeswith(_:).md).

## Parameters

- `attributes`: An array of   objects of kind  . If there are attribute nodes with the same name, the first attribute with that name is used. Send this message with   as   to remove all attributes.

## See Also

- [func addAttribute(XMLNode)](xmlelement/addattribute(_:).md)
  Adds an attribute node to the receiver.
- [func attribute(forName: String) -> XMLNode?](xmlelement/attribute(forname:).md)
  Returns the attribute node of the receiver with the specified name.
- [func attribute(forLocalName: String, uri: String?) -> XMLNode?](xmlelement/attribute(forlocalname:uri:).md)
  Returns the attribute node of the receiver that is identified by a local name and URI.
- [func removeAttribute(forName: String)](xmlelement/removeattribute(forname:).md)
  Removes an attribute node identified by name.
- [func setAttributesWith([String : String])](xmlelement/setattributeswith(_:).md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [func setAttributesAs([AnyHashable : Any])](xmlelement/setattributesas(_:).md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/attributes)*