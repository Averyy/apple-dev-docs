# resolvePrefix(forNamespaceURI:)

**Framework**: Foundation  
**Kind**: method

Returns the prefix associated with the specified URI.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func resolvePrefix(forNamespaceURI namespaceURI: String) -> String?
```

#### Return Value

A string that is the matching prefix or `nil` if it finds no matching prefix.

#### Discussion

The method looks in the entire namespace chain for the URI.

## Parameters

- `namespaceURI`: A string identifying the URI associated with the namespace.

## See Also

- [func addNamespace(XMLNode)](xmlelement/addnamespace(_:).md)
  Adds a namespace node to the receiver.
- [var namespaces: [XMLNode]?](xmlelement/namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func namespace(forPrefix: String) -> XMLNode?](xmlelement/namespace(forprefix:).md)
  Returns the namespace node with a specified prefix.
- [func removeNamespace(forPrefix: String)](xmlelement/removenamespace(forprefix:).md)
  Removes a namespace node that is identified by a given prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](xmlelement/resolvenamespace(forname:).md)
  Returns the namespace node with the prefix matching the given qualified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/resolveprefix(fornamespaceuri:))*