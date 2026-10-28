# resolvePrefix(forNamespaceURI:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the prefix associated with the specified URI.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func resolvePrefix(forNamespaceURI namespaceURI: String) -> String?
```

```objc
- (NSString *) resolvePrefixForNamespaceURI:(NSString *) namespaceURI;
```

## Return Value

A string that is the matching prefix or `nil` if it finds no matching prefix.

## Discussion

The method looks in the entire namespace chain for the URI.

## Parameters

- `namespaceURI`: A string identifying the URI associated with the namespace.

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
- [func resolveNamespace(forName: String) -> XMLNode?](./resolvenamespace%28forname%29.md)
  Returns the namespace node with the prefix matching the given qualified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/resolveprefix(fornamespaceuri:))*