# elements(forLocalName:uri:)

**Framework**: Foundation  
**Kind**: method

Returns the child element nodes (as `NSXMLElement` objects) of the receiver that are matched with the specified local name and URI.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func elements(forLocalName localName: String, uri URI: String?) -> [XMLElement]
```

#### Return Value

An array of `NSXMLElement` objects or an empty array if no matching children could be found.

## Parameters

- `localName`: A string specifying a local name of an element.
- `URI`: A string specifying a URI associated with an element.

## See Also

- [func elements(forName: String) -> [XMLElement]](xmlelement/elements(forname:).md)
  Returns the child element nodes (as `NSXMLElement` objects) of the receiver that have a specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/elements(forlocalname:uri:))*