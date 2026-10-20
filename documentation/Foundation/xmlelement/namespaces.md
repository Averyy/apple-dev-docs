# namespaces

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var namespaces: [XMLNode]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSXMLNode *> * namespaces;
```

## Parameters

- `namespaces`: An array of [`XMLNode`](../xmlnode.md) objects of kind [`XMLNode.Kind.namespace`](../xmlnode/kind-swift.enum/namespace.md).  If there are namespace nodes with the same prefix, the first attribute with that prefix is used. Send this message with `namespaces` as `nil` to remove all namespace nodes.

## See Also

### Handling Namespaces
- [func addNamespace(XMLNode)](./addnamespace%28_%29.md)
  Adds a namespace node to the receiver.
- [func namespace(forPrefix: String) -> XMLNode?](./namespace%28forprefix%29.md)
  Returns the namespace node with a specified prefix.
- [func removeNamespace(forPrefix: String)](./removenamespace%28forprefix%29.md)
  Removes a namespace node that is identified by a given prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](./resolvenamespace%28forname%29.md)
  Returns the namespace node with the prefix matching the given qualified name.
- [func resolvePrefix(forNamespaceURI: String) -> String?](./resolveprefix%28fornamespaceuri%29.md)
  Returns the prefix associated with the specified URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/namespaces)*