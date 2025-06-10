# elements(forName:)

**Framework**: Foundation  
**Kind**: method

Returns the child element nodes (as `NSXMLElement` objects) of the receiver that have a specified name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func elements(forName name: String) -> [XMLElement]
```

#### Return Value

An array of of `NSXMLElement` objects or an empty array if no matching children can be found.

## Parameters

- `name`: A string specifying the name of the child element nodes to find and return. If   is a qualified name, then this method invokes   with the URI parameter set to the URI associated with the prefix. Otherwise comparison is based on string equality of the qualified or non-qualified name.

## See Also

- [func elements(forLocalName: String, uri: String?) -> [XMLElement]](xmlelement/elements(forlocalname:uri:).md)
  Returns the child element nodes (as `NSXMLElement` objects) of the receiver that are matched with the specified local name and URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/elements(forname:))*