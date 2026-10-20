# resolveNamespace(forName:)

**Framework**: Foundation  
**Kind**: method

Returns the namespace node with the prefix matching the given qualified name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func resolveNamespace(forName name: String) -> XMLNode?
```

#### Return Value

An [`XMLNode`](xmlnode.md) object of kind [`XMLNode.Kind.namespace`](xmlnode/kind-swift.enum/namespace.md) or `nil` if there is no matching namespace node.

#### Discussion

The method looks in the entire namespace chain for the prefix.

## Parameters

- `name`: A string that is the qualified name for a namespace (a qualified name is prefix plus local name).

## See Also

- [func addNamespace(XMLNode)](xmlelement/addnamespace(_:).md)
  Adds a namespace node to the receiver.
- [var namespaces: [XMLNode]?](xmlelement/namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func namespace(forPrefix: String) -> XMLNode?](xmlelement/namespace(forprefix:).md)
  Returns the namespace node with a specified prefix.
- [func removeNamespace(forPrefix: String)](xmlelement/removenamespace(forprefix:).md)
  Removes a namespace node that is identified by a given prefix.
- [func resolvePrefix(forNamespaceURI: String) -> String?](xmlelement/resolveprefix(fornamespaceuri:).md)
  Returns the prefix associated with the specified URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/resolvenamespace(forname:))*