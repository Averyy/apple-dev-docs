# removeNamespace(forPrefix:)

**Framework**: Foundation  
**Kind**: method

Removes a namespace node that is identified by a given prefix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func removeNamespace(forPrefix name: String)
```

#### Discussion

The removed XML node object is removed.

## Parameters

- `name`: A string that is the prefix for a namespace.

## See Also

- [func addNamespace(XMLNode)](xmlelement/addnamespace(_:).md)
  Adds a namespace node to the receiver.
- [var namespaces: [XMLNode]?](xmlelement/namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func namespace(forPrefix: String) -> XMLNode?](xmlelement/namespace(forprefix:).md)
  Returns the namespace node with a specified prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](xmlelement/resolvenamespace(forname:).md)
  Returns the namespace node with the prefix matching the given qualified name.
- [func resolvePrefix(forNamespaceURI: String) -> String?](xmlelement/resolveprefix(fornamespaceuri:).md)
  Returns the prefix associated with the specified URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/removenamespace(forprefix:))*