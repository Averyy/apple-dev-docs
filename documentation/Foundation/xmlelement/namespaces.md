# namespaces

**Framework**: Foundation  
**Kind**: property

Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var namespaces: [XMLNode]? { get set }
```

## Parameters

- `namespaces`: An array of   objects of kind  .  If there are namespace nodes with the same prefix, the first attribute with that prefix is used. Send this message with   as   to remove all namespace nodes.

## See Also

- [func addNamespace(XMLNode)](xmlelement/addnamespace(_:).md)
  Adds a namespace node to the receiver.
- [func namespace(forPrefix: String) -> XMLNode?](xmlelement/namespace(forprefix:).md)
  Returns the namespace node with a specified prefix.
- [func removeNamespace(forPrefix: String)](xmlelement/removenamespace(forprefix:).md)
  Removes a namespace node that is identified by a given prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](xmlelement/resolvenamespace(forname:).md)
  Returns the namespace node with the prefix matching the given qualified name.
- [func resolvePrefix(forNamespaceURI: String) -> String?](xmlelement/resolveprefix(fornamespaceuri:).md)
  Returns the prefix associated with the specified URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/namespaces)*