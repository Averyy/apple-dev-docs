# addAttribute(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds an attribute node to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func addAttribute(_ attribute: XMLNode)
```

```objc
- (void) addAttribute:(NSXMLNode *) attribute;
```

#### Discussion

The order of multiple attributes is preserved if the `NSXMLPreserveAttributeOrder` option is specified when the element is created.

## Parameters

- `attribute`: An XML node object representing an attribute. If the receiver already has an attribute with the same name, `anAttribute` replaces the old attribute.

## See Also

### Handling Attributes
- [func attribute(forName: String) -> XMLNode?](./attribute%28forname%29.md)
  Returns the attribute node of the receiver with the specified name.
- [func attribute(forLocalName: String, uri: String?) -> XMLNode?](./attribute%28forlocalname,uri%29.md)
  Returns the attribute node of the receiver that is identified by a local name and URI.
- [var attributes: [XMLNode]?](./attributes.md)
  Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [func removeAttribute(forName: String)](./removeattribute%28forname%29.md)
  Removes an attribute node identified by name.
- [func setAttributesWith([String : String])](./setattributeswith%28_%29.md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [func setAttributesAs([AnyHashable : Any])](./setattributesas%28_%29.md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/addattribute(_:))*