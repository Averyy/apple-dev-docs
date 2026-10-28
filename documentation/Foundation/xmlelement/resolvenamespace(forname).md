# resolveNamespace(forName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the namespace node with the prefix matching the given qualified name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func resolveNamespace(forName name: String) -> XMLNode?
```

```objc
- (NSXMLNode *) resolveNamespaceForName:(NSString *) name;
```

## Return Value

An [`XMLNode`](../xmlnode.md) object of kind [`XMLNode.Kind.namespace`](../xmlnode/kind-swift.enum/namespace.md) or `nil` if there is no matching namespace node.

## Discussion

The method looks in the entire namespace chain for the prefix.

## Parameters

- `name`: A string that is the qualified name for a namespace (a qualified name is prefix plus local name).

## See Also

### Handling Namespaces
- [func addNamespace(XMLNode)](./addnamespace%28_%29.md)
  Adds a namespace node to the receiver.
- [var namespaces: [XMLNode]?](./namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func namespace(forPrefix: String) -> XMLNode?](./namespace%28forprefix%29.md)
  Returns the namespace node with a specified prefix.
- [func removeNamespace(forPrefix: String)](./removenamespace%28forprefix%29.md)
  Removes a namespace node that is identified by a given prefix.
- [func resolvePrefix(forNamespaceURI: String) -> String?](./resolveprefix%28fornamespaceuri%29.md)
  Returns the prefix associated with the specified URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/resolvenamespace(forname:))*