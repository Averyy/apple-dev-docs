# attribute(forLocalName:uri:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the attribute node of the receiver that is identified by a local name and URI.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func attribute(forLocalName localName: String, uri URI: String?) -> XMLNode?
```

```objc
- (NSXMLNode *) attributeForLocalName:(NSString *) localName URI:(NSString *) URI;
```

## Return Value

An XML node object representing a matching attribute or `nil` if no such node was found.

## Parameters

- `localName`: A string specifying the local name of an attribute.
- `URI`: A sting identifying the URI associated with an attribute.

## See Also

### Handling Attributes
- [func addAttribute(XMLNode)](./addattribute%28_%29.md)
  Adds an attribute node to the receiver.
- [func attribute(forName: String) -> XMLNode?](./attribute%28forname%29.md)
  Returns the attribute node of the receiver with the specified name.
- [var attributes: [XMLNode]?](./attributes.md)
  Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [func removeAttribute(forName: String)](./removeattribute%28forname%29.md)
  Removes an attribute node identified by name.
- [func setAttributesWith([String : String])](./setattributeswith%28_%29.md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [func setAttributesAs([AnyHashable : Any])](./setattributesas%28_%29.md)
  Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/attribute(forlocalname:uri:))*