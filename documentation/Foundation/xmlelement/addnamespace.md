# addNamespace(_:)

**Framework**: Foundation  
**Kind**: method

Adds a namespace node to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func addNamespace(_ aNamespace: XMLNode)
```

## Parameters

- `aNamespace`: An XML node object of kind  . If the receiver already has a namespace with the same name,   is not added.

## See Also

- [var namespaces: [XMLNode]?](xmlelement/namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func namespace(forPrefix: String) -> XMLNode?](xmlelement/namespace(forprefix:).md)
  Returns the namespace node with a specified prefix.
- [func removeNamespace(forPrefix: String)](xmlelement/removenamespace(forprefix:).md)
  Removes a namespace node that is identified by a given prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](xmlelement/resolvenamespace(forname:).md)
  Returns the namespace node with the prefix matching the given qualified name.
- [func resolvePrefix(forNamespaceURI: String) -> String?](xmlelement/resolveprefix(fornamespaceuri:).md)
  Returns the prefix associated with the specified URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/addnamespace(_:))*