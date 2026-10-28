# setAttributesAs(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: This method is deprecated because it does not function properly. Instead use [`setAttributesWith(_:)`](./setattributeswith%28_%29.md).

## Declaration

```swift
func setAttributesAs(_ attributes: [AnyHashable : Any])
```

```objc
- (void) setAttributesAsDictionary:(NSDictionary *) attributes;
```

## Discussion

The method uses these names and object values to create [`XMLNode`](../xmlnode.md) objects of kind [`XMLNode.Kind.attribute`](../xmlnode/kind-swift.enum/attribute.md). Existing attributes are not removed.

## Parameters

- `attributes`: A dictionary of key-value pairs where the attribute name is the key and the object value of the attribute is the dictionary value.

## See Also

### Handling Attributes
- [func addAttribute(XMLNode)](./addattribute%28_%29.md)
  Adds an attribute node to the receiver.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/setattributesas(_:))*