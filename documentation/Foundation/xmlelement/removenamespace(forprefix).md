# removeNamespace(forPrefix:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes a namespace node that is identified by a given prefix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func removeNamespace(forPrefix name: String)
```

```objc
- (void) removeNamespaceForPrefix:(NSString *) name;
```

## Discussion

The removed XML node object is removed.

## Parameters

- `name`: A string that is the prefix for a namespace.

## See Also

### Handling Namespaces
- [func addNamespace(XMLNode)](./addnamespace%28_%29.md)
  Adds a namespace node to the receiver.
- [var namespaces: [XMLNode]?](./namespaces.md)
  Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [func namespace(forPrefix: String) -> XMLNode?](./namespace%28forprefix%29.md)
  Returns the namespace node with a specified prefix.
- [func resolveNamespace(forName: String) -> XMLNode?](./resolvenamespace%28forname%29.md)
  Returns the namespace node with the prefix matching the given qualified name.
- [func resolvePrefix(forNamespaceURI: String) -> String?](./resolveprefix%28fornamespaceuri%29.md)
  Returns the prefix associated with the specified URI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/removenamespace(forprefix:))*