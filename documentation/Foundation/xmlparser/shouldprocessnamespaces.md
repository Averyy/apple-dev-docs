# shouldProcessNamespaces

**Framework**: Foundation  
**Kind**: property

A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var shouldProcessNamespaces: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the parser reports namespace and qualified name, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

The parser reports element names with the delegate methods [`parser(_:didStartElement:namespaceURI:qualifiedName:attributes:)`](xmlparserdelegate/parser(_:didstartelement:namespaceuri:qualifiedname:attributes:).md) and [`parser(_:didEndElement:namespaceURI:qualifiedName:)`](xmlparserdelegate/parser(_:didendelement:namespaceuri:qualifiedname:).md).

## See Also

- [var shouldReportNamespacePrefixes: Bool](xmlparser/shouldreportnamespaceprefixes.md)
  A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.
- [var shouldResolveExternalEntities: Bool](xmlparser/shouldresolveexternalentities.md)
  A Boolean value that determines whether the parser reports declarations of external entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/shouldprocessnamespaces)*