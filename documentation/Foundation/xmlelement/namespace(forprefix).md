# namespace(forPrefix:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the namespace node with a specified prefix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func namespace(forPrefix name: String) -> XMLNode?
```

```objc
- (NSXMLNode *) namespaceForPrefix:(NSString *) name;
```

## Return Value

An [`XMLNode`](../xmlnode.md) object of kind [`XMLNode.Kind.namespace`](../xmlnode/kind-swift.enum/namespace.md) or `nil` if there is no namespace node with that prefix.

## Parameters

- `name`: A string specifying a namespace prefix.

## See Also

### Handling Namespaces
- [func addNamespace(XMLNode)](./addnamespace%28_%29.md)
  Adds a namespace node to the receiver.
- [var namespaces: [XMLNode]?](./namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func removeNamespace(forPrefix: String)](./removenamespace%28forprefix%29.md)
  Removes a namespace node that is identified by a given prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](./resolvenamespace%28forname%29.md)
  Returns the namespace node with the prefix matching the given qualified name.
- [func resolvePrefix(forNamespaceURI: String) -> String?](./resolveprefix%28fornamespaceuri%29.md)
  Returns the prefix associated with the specified URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/namespace(forprefix:))*