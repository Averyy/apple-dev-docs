# addNamespace(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a namespace node to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func addNamespace(_ aNamespace: XMLNode)
```

```objc
- (void) addNamespace:(NSXMLNode *) aNamespace;
```

## Parameters

- `aNamespace`: An XML node object of kind [`XMLNode.Kind.namespace`](../xmlnode/kind-swift.enum/namespace.md). If the receiver already has a namespace with the same name, `aNamespace` is not added.

## See Also

### Handling Namespaces
- [var namespaces: [XMLNode]?](./namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func namespace(forPrefix: String) -> XMLNode?](./namespace%28forprefix%29.md)
  Returns the namespace node with a specified prefix.
- [func removeNamespace(forPrefix: String)](./removenamespace%28forprefix%29.md)
  Removes a namespace node that is identified by a given prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](./resolvenamespace%28forname%29.md)
  Returns the namespace node with the prefix matching the given qualified name.
- [func resolvePrefix(forNamespaceURI: String) -> String?](./resolveprefix%28fornamespaceuri%29.md)
  Returns the prefix associated with the specified URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/addnamespace(_:))*