# attributes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets all attributes of the receiver at once, replacing any existing attribute nodes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var attributes: [XMLNode]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSXMLNode *> * attributes;
```

#### Discussion

To set attributes in an element node using an [`NSDictionary`](../nsdictionary.md) object as the input parameter, see [`setAttributesWith(_:)`](./setattributeswith%28_%29.md).

## Parameters

- `attributes`: An array of [`XMLNode`](../xmlnode.md) objects of kind [`XMLNode.Kind.attribute`](../xmlnode/kind-swift.enum/attribute.md). If there are attribute nodes with the same name, the first attribute with that name is used. Send this message with `attributes` as `nil` to remove all attributes.

## See Also

### Handling Attributes
- [func addAttribute(XMLNode)](./addattribute%28_%29.md)
  Adds an attribute node to the receiver.
- [func attribute(forName: String) -> XMLNode?](./attribute%28forname%29.md)
  Returns the attribute node of the receiver with the specified name.
- [func attribute(forLocalName: String, uri: String?) -> XMLNode?](./attribute%28forlocalname,uri%29.md)
  Returns the attribute node of the receiver that is identified by a local name and URI.
- [func removeAttribute(forName: String)](./removeattribute%28forname%29.md)
  Removes an attribute node identified by name.
- [func setAttributesWith([String : String])](./setattributeswith%28_%29.md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [func setAttributesAs([AnyHashable : Any])](./setattributesas%28_%29.md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/attributes)*